CAMERA_STEP = 10


class Camera:
    width = 0
    height = 0
    x = 0
    y = 0
    zoom = 1.0
    canvas = None
    map = None

    def __init__(self, canvas=None, the_map=None, width=800, height=600):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.zoom = 1.0
        if canvas is not None:
            self.canvas = canvas
        if the_map is not None:
            self.map = the_map

    def up(self, event):
        self.y -= CAMERA_STEP
        self.draw()

    def down(self, event):
        self.y += CAMERA_STEP
        self.draw()

    def left(self, event):
        self.x -= CAMERA_STEP
        self.draw()

    def right(self, event):
        self.x += CAMERA_STEP
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        for self.tile in self.map.tiles:
            tl_x = self.tile.x - self.x
            tl_y = self.tile.y - self.y
            br_x = self.tile.x + self.tile.width - self.x
            br_y = self.tile.y + self.tile.height - self.y
            self.tile.id = self.canvas.create_image(tl_x, tl_y, image=self.tile.image.image, anchor="nw")
            self.canvas.create_rectangle(tl_x, tl_y, br_x, br_y, width=0.5)
            overlapping = self.canvas.find_overlapping(self.x, self.y, self.x + self.width, self.y + self.y)
            if self.tile.id not in overlapping:
                self.canvas.delete(self.tile)
