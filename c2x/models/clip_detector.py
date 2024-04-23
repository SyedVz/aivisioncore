from c2x.base.segmentation import Segmentation
from c2x.base.detector import Detector

import torch
import cv2 as cv
import numpy as np
from torchvision import transforms
from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation
import torchvision.transforms.functional as F


def get_padding(sz):
    max_wh = np.max(sz)
    hp = int((max_wh - sz[-1]) / 2)
    vp = int((max_wh - sz[-2]) / 2)
    padding = (hp, vp, hp, vp)
    return padding


class CLIPDetector(Detector):
    def __init__(self, queries=None):
        self.processor = CLIPSegProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
        self.model = CLIPSegForImageSegmentation.from_pretrained("CIDAS/clipseg-rd64-refined")
        self.preprocess = None
        self.postprocess = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.model.to(self.device)
        self.queries = queries
        
        if not queries:
            self.queries = ["road sign", "vehicle"]
            
        self.inputs = self.processor(text=self.queries, return_tensors='pt', padding="max_length").to(self.device)

    
    def detect(self, frame):
        if self.preprocess == None:
            sz = np.array(frame.shape[:2])
            # Cast to regular ints, some versions don't like np.int32 elems
            scaled_sz = [int(d) for d in (sz * 352 / max(sz))]
            padding = get_padding(scaled_sz)

            self.preprocess = transforms.Compose([
                transforms.Resize(scaled_sz, transforms.InterpolationMode.BILINEAR, antialias=True),
                transforms.Pad(padding), # Letterboxing
                # transforms.Pad((scaled_sz[1] % 2, scaled_sz[0] % 2, 0, 0)),
                # transforms.CenterCrop(352),
                transforms.Lambda(lambda x : x / 255.),
                # transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
            ])

            self.postprocess = transforms.Compose([
                transforms.CenterCrop(scaled_sz),
            ])

        in_tensor = torch.from_numpy(frame).to(self.device).permute(2, 0, 1).unsqueeze(0)[:, [2, 1, 0], :, :]
        pixel_inputs = self.preprocess(in_tensor)
        self.inputs["pixel_values"] = pixel_inputs.repeat(len(self.queries), 1, 1, 1)
        
        with torch.no_grad():
            outputs = self.model(**self.inputs)
            preds = outputs.logits.unsqueeze(1 if len(self.queries) > 1 else 0)
            if len(preds.shape) == 3:
                preds = preds.unsqueeze(0)

            preds = torch.sigmoid(preds)
            # preds = torch.softmax(preds, dim=0)
            preds = self.postprocess(preds)
            # labels = preds.argmax(dim=0)[0]

        out_boxes = []
        out_classes = []
        out_probs = []
        out_contours = []
        im_area = preds.shape[-1] * preds.shape[-2]
        a_thresh = im_area * 0.001
        conf_thresh = 0.66 / len(self.queries)

        for i, p in enumerate(preds):
            cp = p[0]# * (labels == i) # Corresponding to query i
            # if len(cp) == 0:
            #     continue

            # disp = (cp.cpu().numpy() * 255).astype(np.uint8)
            # disp = cv.cvtColor(disp, cv.COLOR_GRAY2BGR)
            cp[cp < conf_thresh] = 0
            cp[cp >= conf_thresh] = 1
            # disp = (cp.cpu().numpy() * 255).astype(np.uint8)
            # disp = cv.cvtColor(disp, cv.COLOR_GRAY2BGR)
            label = self.queries[i]
            mask = (cp.cpu().numpy() * 255).astype(np.uint8)
            # totalLabels, _, values, _ = cv.connectedComponentsWithStats(mask, 4, cv.CV_32S)
            contours, hierarchy = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
            # cv.drawContours(disp, contours, -1, (0, 255, 0), 1)

            for idx in range(0, len(contours)): #totalLabels
                # row = values[idx,:]
                # if row[cv.CC_STAT_AREA] < a_thresh:
                #     continue
                # bb = np.array([row[cv.CC_STAT_LEFT], row[cv.CC_STAT_TOP], row[cv.CC_STAT_WIDTH], row[cv.CC_STAT_HEIGHT]])

                ct = contours[idx]
                if cv.contourArea(ct) < a_thresh:
                    continue

                bb = np.array(cv.boundingRect(ct))

                # cv.rectangle(disp, bb, (255,255,255), 1, cv.LINE_AA)
                bb = (max(frame.shape) * bb / 352).astype(int)
                ct = (ct * max(frame.shape) / 352).astype(int)
                out_boxes.append(bb)
                out_classes.append(label)
                out_probs.append(1) # Dummy value, TODO: Calculate from mask
                out_contours.append(ct)

            # cv.imshow(f'{self.queries[i]}', disp)

        return Segmentation(out_boxes, out_classes, out_probs, out_contours)