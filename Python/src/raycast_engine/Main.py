import tkinter as tk

from Game.GameHandler import GameHandler
from Renderer import Renderer


# pls make more comments + idk whats supposed to happen
# my method of runnning: cd ~/Documents/GitHub/Raycasting-Engine/Python/src/raycast_engine, python3 Main.py
class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Raycast Engine")
        self.canvas = tk.Canvas(self.window, height=800, width=1550, bg="black")
        self.canvas.pack()
        self.renderer = Renderer(self)
        self.objectsToTick = []
        self.game = GameHandler(self)

    def addToTickList(self, object):
        self.objectsToTick.append(object)

    def tick(self):
        self.canvas.delete("all")
        print("hello")
        for object in self.objectsToTick:
            object.tick()
            print(str(self.renderer.tick))
        self.renderer.tick()
        self.window.update()


world = Main()

world.window.after(1, world.tick)
world.window.mainloop()
