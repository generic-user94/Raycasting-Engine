import tkinter as tk

from Python.src.raycast_engine.Renderer import Renderer
from Python.src.raycast_engine.Game.GameHandler import GameHandler

class Main():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Raycast Engine')
        self.canvas = tk.Canvas(self.window, height=750, width=1500, bg='black')
        self.canvas.pack()
        self.renderer = Renderer(self)
        self.objectsToTick = []
        self.game = GameHandler(self)
        self.game.loadLevel(0)

    def addToTickList(self, object):
        self.objectsToTick.append(object)

    def tick(self):
        self.canvas.delete('all')
        for object in self.objectsToTick:
            object.tick()
        self.renderer.tick()
        self.window.update()
        world.window.after(5, world.tick)


world = Main()
world.window.after(5, world.tick)
world.window.mainloop()