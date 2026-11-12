from Python.src.raycast_engine.Game.BoundingBox import BoundingBox
from Python.src.raycast_engine.Util import getPointInDir


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
            dx, dy = getPointInDir(0, 0, 100 * self.game.world.deltaTime, self.dir - 90)
            dx = int(dx)
            dy = int(dy)

        for x in range(abs(dx)):
            self.hitbox.move(self.hitbox.x1 + 1*(abs(dx)/dx), self.hitbox.y1)
            if self.game.ground.hitsBox(self.hitbox):
                self.hitbox.move(self.hitbox.x1 - 1*(abs(dx)/dx), self.hitbox.y1)
                break
            else:
                self.x += 1*(abs(dx)/dx)

        for x in range(abs(dy)):
            print('moved up')
            self.hitbox.move(self.hitbox.x1, self.hitbox.y1 + 1*(abs(dy)/dy))
            if self.game.ground.hitsBox(self.hitbox):
                self.hitbox.move(self.hitbox.x1, self.hitbox.y1 - 1*(abs(dy)/dy))
                break
            else:
                self.y += 1*(abs(dy)/dy)



        if 'q' in self.game.keys:
            self.dir -= 100 * self.game.world.deltaTime
        if 'e' in self.game.keys:
            self.dir += 100 * self.game.world.deltaTime