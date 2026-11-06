from Level.Ground import Ground
from Level.Levels import Level


class GameHandler:
    def __init__(self, world):
        self.world = world
        self.ground = Ground(self)
        # hit

    def loadLevel(self, map):
        self.ground.clear()
        # not hit, is it supposed to
        maps = Level()
        level = maps.getLevel(map)
        for rect in level:
            self.ground.addBox(rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])
