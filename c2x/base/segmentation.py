from c2x.base.detection import Detection

class Segmentation(Detection):
    def __init__(self, boxes = [], classes = [], probs=[], contours=[]):
        super().__init__(boxes, classes, probs)
        self.contours = contours

    
    def get_contours(self):
        return self.contours
    

    def __iter__(self):
        return zip(self.boxes.__iter__(), self.classes.__iter__(), 
                   self.probs.__iter__(), self.contours.__iter__())


    def __next__(self):
        return zip(self.boxes.__next__(), self.classes.__next__(), 
                   self.probs.__next__(), self.contours.__next__())
    

    def __len__(self):
        return len(self.boxes)
    

    def __str__(self):
        return f'Segmentation: {len(self)} items'
