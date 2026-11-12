from Python.src.raycast_engine.Raycasting.Caster import Caster
from Python.src.raycast_engine.Settings import Settings
from Python.src.raycast_engine.Util import getPointInDir

class Renderer():
    def __init__(self, world):
        self.world = world
        self.caster = Caster(self.world.game)

    def tick(self):
        self.caster.cast()
        self.draw()
        self.renderMap()
        self.renderPlayer()
        self.flashlight()


    def renderMap(self):
        map = self.world.game.ground
        for box in map.boxes:
            self.world.canvas.create_rectangle(box.x1, box.y1, box.x2, box.y2, fill = 'white', width=0)

    def renderPlayer(self):
        player = self.world.game.player
        self.world.canvas.create_polygon(player.x, player.y-20, player.x-10, player.y+10, player.x+10, player.y+10, fill = 'green')

    def flashlight(self):
        counter = 0
        for dist in self.caster.dists:
            x, y = getPointInDir(self.world.game.player.x, self.world.game.player.y, dist,
                                 (Settings.FOV/-2 + self.world.game.player.dir - 90)
                                  + ((Settings.FOV/Settings.QUALITY) * counter))
            self.world.canvas.create_line(self.world.game.player.x, self.world.game.player.y, x, y, fill = 'blue')
            counter += 1

    def draw(self):
        idx = 0
        width = 1500/Settings.QUALITY
        for dist in self.caster.dists:

            x1 = idx * width
            y1 = 800 - dist/2
            x2 = x1 + width
            y2 = 800 - y1

            self.world.canvas.create_rectangle(x1, y1, x2, y2, fill='white', width = 0)

            idx += 1
