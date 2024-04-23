import os
from c2x.base.detection import Detection
from c2x.base.detector import Detector
import numpy as np
import torch
import yolov7 #https://github.com/kadirnar/yolov7-pip
from yolov7.utils.general import non_max_suppression
from torchvision import transforms


def get_padding(sz):
    max_wh = np.max(sz)
    hp = int((max_wh - sz[-1]) / 2)
    vp = int((max_wh - sz[-2]) / 2)
    padding = (hp, vp, hp, vp)
    return padding


class YoloDetector(Detector):
    def __init__(self, weights='yolov7'):
        this_dir = os.path.dirname(__file__)
        root_dir = os.path.dirname(this_dir)
        weights_file = os.path.join(root_dir, "assets", f'{weights}.pt')
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f'Using device: {self.device}')
        self.preprocess = None
        self.postprocess = None
        self.proc_size = 320 # reduce this to speed up detection?
        self.model = yolov7.load(weights_file, device=self.device, size=self.proc_size)
        self.conf = 0.54  # NMS confidence threshold
        self.iou = 0.50  # NMS IoU threshold
        self.classes = None  # (optional list) filter by class
        self.paddingTensor = None
        self.scalingTensor = None
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names

    
    def detect(self, frame):
        if self.preprocess == None:
            # Cast to regular ints, some versions don't like np.int32 elems
            sz = np.array(frame.shape[:2])
            scaled_sz = [int(d) for d in (sz * self.proc_size / max(sz))]
            scaled_sz = [self.proc_size, self.proc_size]
            padding = get_padding(scaled_sz)

            self.preprocess = transforms.Compose([
                transforms.Resize(scaled_sz, transforms.InterpolationMode.BILINEAR, antialias=True),
                transforms.Pad(padding), # Letterboxing
                transforms.Lambda(lambda x : x / 255.),
                # transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
            ])

            self.paddingTensor = torch.Tensor([[padding[0], padding[1], 0, 0]]).to(self.device)
            self.scalingTensor = torch.Tensor(np.array([sz[::-1] / scaled_sz[::-1]])).to(self.device).repeat(1, 2)

        in_tensor = torch.from_numpy(frame).to(self.device).permute(2, 0, 1).unsqueeze(0)[:, [2, 1, 0], :, :]
        in_tensor = self.preprocess(in_tensor)
        
        with torch.no_grad():
            y = self.model(in_tensor)[0]
            y = non_max_suppression(y, conf_thres=self.conf, iou_thres=self.iou, classes=self.classes)  # NMS

        if len(y) == 0:
            return Detection()
        
        # parse results
        predictions = y[0]
        boxes = predictions[:, :4] # x1, y1, x2, y2
        boxes[:, 2:] -= boxes[:, :2]
        boxes -= self.paddingTensor
        boxes = self.scalingTensor * boxes
        boxes = boxes.cpu().numpy()
        scores = predictions[:, 4]
        categories = predictions[:, 5]

        out_boxes = []
        out_classes = []
        out_scores = []

        for idx in range(len(boxes)):
            bb = boxes[idx,:].astype(int)
            out_boxes.append(bb)
            out_classes.append(self.names[int(categories[idx])])
            out_scores.append(scores[idx])

        return Detection(out_boxes, out_classes, out_scores)