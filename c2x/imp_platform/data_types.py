from enum import Enum


class ImageDetection(Enum):
    pedestrian = 'pedestrian'
    traffic_light = 'traffic_light'
    traffic_sign = 'traffic_sign'
    vehicle = 'vehicle'
    traffic_cone = "traffic_cone"

    def __str__(self):
        return f'{self.value}'
    

class DetectionExtents:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


class IncidentsName(Enum):
    explosion = 'explosion'
    accident = 'accident'
    fogwarning ='fogwarning'
    congestion ='congestion'
    violation = 'violation'
    notmatching = 'not matching'
    constructionzone = "construction zone"
    custom_1 = "custom_incident_1"

    def __str__(self):
        return f'{self.value}'
