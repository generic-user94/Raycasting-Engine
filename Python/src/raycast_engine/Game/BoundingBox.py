


class BoundingBox():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y2

    def move(self, x, y):
        self.x1 = x
        self.y1 = y
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height

    def hits(self, x, y):
        if self.x1 < x < self.x2 and self.y1 < y < self.y2:
            return True
        else:
            return False

    def hitsBox(self, box):
        if self.x1 < box.x1 < self.x2 or self.x1 < box.x2 < self.x2:
            if self.y1 < box.y1 < self.y2 or self.y1 < box.y2 < self.y2:
                return True
        return False


    def containsBox(self, box):
        if self.x1 < box.x1 < self.x2 and self.x1 < box.x2 < self.x2:
            if self.y1 < box.y1 < self.y2 and self.y1 < box.y2 < self.y2:
                return True
        return False