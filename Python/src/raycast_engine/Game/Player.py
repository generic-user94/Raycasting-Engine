


class Player():
    def __init__(self, x, y, game):
        self.x, self.y = x, y
        self.dir = 0
        self.game = game
        self.game.world.addToTickList(self)

    def tick(self):
        self.move()

    def move(self):
        if 'w' in self.game.keys:
            self.y -= 1
        if 's' in self.game.keys:
            self.y += 1
        if 'a' in self.game.keys:
            self.x -= 1
        if 'd' in self.game.keys:
            self.x += 1