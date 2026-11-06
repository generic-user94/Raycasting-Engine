from Python.src.raycast_engine.Game.BoundingBox import BoundingBox


class Ground():
    def __init__(self, game):
        self.game = game
        self.game.world.addToTickList(self)
        self.boxes = []

    def tick(self):
        pass

    def addBox(self, x1, y1, x2, y2):
        self.boxes.append(BoundingBox(x1, y1, abs(x1-x2), abs(y1-y2)))

    def clear(self):
        self.boxes = []

    def hits(self, x, y):
        for box in self.boxes:
            if box.hits(x, y):
                return True
        return False

    def hitsBox(self, box):
        for ground in self.boxes:
            if ground.hitsBox(box):
                return True
        return False

    def containsBox(self, box):
        for ground in self.boxes:
            if ground.containsBox(box):
                return True
        return False