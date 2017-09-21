from tkinter import *

from com.federicofeliziani.dnd.client.ImageStore import ImageStore
from com.federicofeliziani.dnd.client.MapLoader import MapLoader
from com.federicofeliziani.dnd.client.entities.Camera import Camera


class App:
    FULL_SCREEN = True
    IMAGE_STORE = None

    def __init__(self, master):
        if self.IMAGE_STORE is None:
            self.IMAGE_STORE = ImageStore()
        self.master = master
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        master.bind('<Escape>', self.toggle_fullscreen)

        frame = Frame(master)
        frame.pack()

        canvas = Canvas(frame, bg="black", width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        canvas.pack()
        self.map = MapLoader.load("map3")
        camera = Camera(canvas=canvas, the_map=self.map)

        master.bind('<Up>', camera.up)
        master.bind('<Down>', camera.down)
        master.bind('<Left>', camera.left)
        master.bind('<Right>', camera.right)

        camera.draw()

    @staticmethod
    def toggle_fullscreen(event):
        App.FULL_SCREEN = not App.FULL_SCREEN
        root.attributes("-fullscreen", App.FULL_SCREEN)


root = Tk()

root.attributes('-fullscreen', App.FULL_SCREEN)

app = App(root)

root.mainloop()
