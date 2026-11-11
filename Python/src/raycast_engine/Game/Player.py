from Python.src.raycast_engine.Game.BoundingBox import BoundingBox


class Player():
    def __init__(self, x, y, game):
        self.x, self.y = x, y
        self.dir = 0
        self.game = game
        self.game.world.addToTickList(self)
        self.hitbox = BoundingBox(self.x - 10, self.y - 20, self.x + 10, self.y + 10)

    def tick(self):
        self.move()

    def move(self):
        dx = 0
        dy = 0
        if 'w' in self.game.keys:
            dy -= 2
        if 's' in self.game.keys:
            dy += 2
        if 'a' in self.game.keys:
            dx -= 2
        if 'd' in self.game.keys:
            dx += 2

        self.hitbox.move(self.hitbox.x1 + dx, self.hitbox.y1)
        if not self.game.ground.hitsBox(self.hitbox):
            self.x += dx
        else:
            self.hitbox.move(self.hitbox.x1 - dx, self.hitbox.y1)

        self.hitbox.move(self.hitbox.x1, self.hitbox.y1 + dy)
        if not self.game.ground.hitsBox(self.hitbox):
            self.y += dy
        else:
            self.hitbox.move(self.hitbox.x1, self.hitbox.y1 - dy)