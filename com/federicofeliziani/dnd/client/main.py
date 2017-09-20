from tkinter import *

from com.federicofeliziani.dnd.client.MapLoader import MapLoader


class App:
    FULL_SCREEN = True

    def __init__(self, master):
        self.master = master
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        master.bind('<Escape>', self.toggle_fullscreen)

        frame = Frame(master)
        frame.pack()

        canvas = Canvas(frame, bg="black", width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        canvas.pack()
        self.map = MapLoader.load("map3")
        for self.tile in self.map.tiles:
            canvas.create_image(self.tile.x * self.tile.width, self.tile.y * self.tile.height, image=self.tile.image, anchor="nw")
            canvas.create_rectangle(self.tile.x * self.tile.width, self.tile.y * self.tile.height, (self.tile.x * self.tile.width) + self.tile.width, (self.tile.y * self.tile.height) + self.tile.height, width=0.5)

    @staticmethod
    def toggle_fullscreen(event):
        App.FULL_SCREEN = not App.FULL_SCREEN
        root.attributes("-fullscreen", App.FULL_SCREEN)


root = Tk()

root.attributes('-fullscreen', App.FULL_SCREEN)

app = App(root)

root.mainloop()
