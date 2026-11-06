from Python.src.raycast_engine.Level.Ground import Ground
from Python.src.raycast_engine.Level.Levels import Level


class GameHandler():
    def __init__(self, world):
        self.world = world
        self.ground = Ground(self)

    def loadLevel(self, map):
        self.ground.clear()
        maps = Level()
        level = maps.getLevel(map)
        for rect in level:
            self.ground.addBox(rect[0], rect[1], rect[2]-rect[0], rect[3] - rect[1])
