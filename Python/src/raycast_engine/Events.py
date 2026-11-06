


class Events():
    def __init__(self, window, game):
        self.game = game
        window.bind("<KeyPress>", self.onKeyPress)
        window.bind("<KeyRelease>", self.onKeyRelease)


    def onKeyPress(self, event):
        if not event.keysym in self.game.keys:
            self.game.keys.append(event.keysym)

    def onKeyRelease(self, event):
        if event.keysym in self.game.keys:
            self.game.keys.remove(event.keysym)
