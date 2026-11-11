from Python.src.raycast_engine.Raycasting.Ray import Ray
from Python.src.raycast_engine.Settings import Settings


class Caster():
    def __init__(self, game):
        self.game = game
        self.dists = []

    def cast(self):
        self.dists = []
        player = self.game.player
        baseDir = Settings.FOV/-2 + player.dir - 90
        for x in range(Settings.QUALITY+1):
            ray = Ray(player.x, player.y, baseDir + ((Settings.FOV/Settings.QUALITY) * x), self.game)
            self.dists.append(ray.getDist())