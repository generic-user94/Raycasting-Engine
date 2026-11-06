import tkinter as tk

from Python.src.raycast_engine.Renderer import Renderer
from Python.src.raycast_engine.Game.GameHandler import GameHandler

class Main():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Raycast Engine')
        self.canvas = tk.Canvas(self.window, height=800, width=1550, bg='black')
        self.canvas.pack()
        self.renderer = Renderer(self)
        self.objectsToTick = []
        self.game = GameHandler(self)

    def addToTickList(self, object):
        self.objectsToTick.append(object)

    def tick(self):
        self.canvas.delete('all')
        print('hello')
        for object in self.objectsToTick:
            object.tick()
        self.renderer.tick()
        self.window.update()


world = Main()
world.window.after(0, world.tick)
world.window.mainloop()