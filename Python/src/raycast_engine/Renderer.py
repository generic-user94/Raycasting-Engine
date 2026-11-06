


class Renderer():
    def __init__(self, world):
        self.world = world

    def tick(self):
        self.renderMap()
        self.renderPlayer()


    def renderMap(self):
        map = self.world.game.ground
        for box in map.boxes:
            self.world.canvas.create_rectangle(box.x1, box.y1, box.x2, box.y2, fill = 'white', width=0)

    def renderPlayer(self):
        player = self.world.game.player
        self.world.canvas.create_polygon(player.x, player.y-20, player.x-10, player.y+10, player.x+10, player.y+10, fill = 'white', width = 0)