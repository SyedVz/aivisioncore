class Detection():
    def __init__(self, boxes = [], classes = [], probs = []):
        assert len(boxes) == len(classes)
        self.boxes = boxes
        self.classes = classes
        self.probs = probs

    
    def get_boxes(self):
        return self.boxes
    
    
    def get_classes(self):
        return self.classes
    

    def get_probs(self):
        return self.probs
    

    def __iter__(self):
        return zip(self.boxes.__iter__(), self.classes.__iter__(), self.probs.__iter__())


    def __next__(self):
        return zip(self.boxes.__next__(), self.classes.__next__(), self.probs.__next__())
    

    def __len__(self):
        return len(self.boxes)
