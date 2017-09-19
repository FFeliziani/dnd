from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        canvas = Canvas(frame, bg="black", width=500, height=500)
        canvas.pack()

        self.photo_image = PhotoImage(file=r'resources/images/dirt.png')
        canvas.create_image(250, 250, image=self.photo_image)


root = Tk()

app = App(root)

root.mainloop()
