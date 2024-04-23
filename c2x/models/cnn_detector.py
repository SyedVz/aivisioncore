from c2x.base.detection import Detection
from c2x.base.detector import Detector
import torch
from torch import nn
from torchvision.models.detection import ssdlite320_mobilenet_v3_large
from torchvision.models.detection import SSDLite320_MobileNet_V3_Large_Weights
# from torchinfo import summary



class CNNDetector(Detector):
    def __init__(self, numClasses):
        super(CNNDetector, self).__init__()
        weights_url="https://download.pytorch.org/models/ssdlite320_mobilenet_v3_large_coco-a79551df.pth"
        # weights_backbone_url="https://download.pytorch.org/models/mobilenet_v3_large-5c1a4163.pth"
        weights = torch.hub.load_state_dict_from_url(weights_url, progress=True)
        # weights_backbone = torch.hub.load_state_dict_from_url(weights_backbone_url, progress=True)

        keys = list(weights.keys())
        for k in keys:
            if any([s in k.lower() for s in ['head', 'backbone.features', 'backbone.extra']]):
                w = weights[k]
                print(f'{k}: {w.shape}')
                del weights[k]

        self.model = ssdlite320_mobilenet_v3_large(num_classes=numClasses)
        self.model.load_state_dict(weights, strict=False)
        self.model.eval()
        # torch.onnx.export(self.model, torch.randn((1, 3, 320, 320)), 'ssdlite_mobilnet_v3.onnx')
        # summary(self.model, (1, 3, 320, 320), verbose=1, depth=3, col_names=["kernel_size", "output_size", "num_params"])

    
    def detect(self, frame) -> Detection:
        return Detection()