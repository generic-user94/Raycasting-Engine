from Python.src.raycast_engine.Util import getPointInDir, distance

from Python.src.raycast_engine.Game.BoundingBox import BoundingBox


class Ray():
    def __init__(self, x, y, dir, game):
        self.game = game
        self.dist = 10
        self.dir = dir
        self.box = BoundingBox(x-1, y-1, x+1, y+1)
        self.x, self.y = x, y
        self.cast()

    def getDist(self):
        return self.dist

    def cast(self):
        while True:
            x, y = getPointInDir(self.box.x1 + 1, self.box.y1 + 1, 10, self.dir)
            self.box.move(x - 1, y - 1)
            if self.game.ground.hitsBox(self.box):
                x, y = getPointInDir(self.box.x1 + 1, self.box.y1 + 1, -10, self.dir)
                self.box.move(x - 1, y - 1)
                while True:
                    x, y = getPointInDir(self.box.x1 + 1, self.box.y1 + 1, 1, self.dir)
                    self.box.move(x - 1, y - 1)
                    if self.game.ground.hitsBox(self.box):
                        break
                break
        self.dist = distance(self.x, self.y, self.box.x1 + 1, self.box.y1 + 1)