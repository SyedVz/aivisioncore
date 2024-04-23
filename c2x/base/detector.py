from abc import ABC, abstractmethod
from c2x.base.detection import Detection


class Detector(ABC):

    @abstractmethod
    def detect(self, frame) -> Detection:
        pass