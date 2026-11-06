


class Renderer():
    def __init__(self, world):
        self.world = world

    def tick(self):
        self.renderMap()


    def renderMap(self):
        map = self.world.game.ground
        for box in map.boxes:
            self.world.canvas.create_rectangle(box.x1, box.y1, box.x2, box.y2, bg = 'white')
