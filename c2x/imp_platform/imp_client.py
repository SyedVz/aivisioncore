from .data_types import ImageDetection
from .data_types import DetectionExtents


class IMPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    
    def is_valid(self):
        return True


    def send_image_detection(self, type: ImageDetection, extents: DetectionExtents):
        # print(f'Sending image detection: {type} at {extents.x}, {extents.y}, {extents.w}, {extents.h}')
        return True