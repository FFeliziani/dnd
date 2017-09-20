from PIL import ImageTk, Image

IMAGE_LIST = []


class Tile:
    index = 0
    x = 0
    y = 0
    width = 0
    height = 0
    type = None
    image = None

    def __init__(self, x=None, y=None, position=None, width=None, height=None, size=None, tile_type="Dirt", index=None):
        if position is None and x is not None and y is not None:
            self.x = x
            self.y = y
        if position is not None and x is None and y is None:
            self.x = position.x
            self.y = position.y
        if x is None and y is None and position is None:
            self.x = 0
            self.y = 0
        if size is None and width is not None and height is not None:
            self.width = width
            self.height = height
        if width is None and height is None and size is not None:
            self.width = size.width
            self.height = size.height
        if width is None and height is None and size is None:
            self.width = 0
            self.height = 0
        if index is not None:
            self.index = index
        self.type = TileType.by_name(TileType(), name=tile_type)
        found = False
        for img in IMAGE_LIST:
            if img.path == self.type.path:
                self.image = img.image
                found = True
        if not found:
            img = TileImage(path=self.type.path, image=ImageTk.PhotoImage(Image.open(self.type.path).resize(self.size_as_tuple(), Image.ANTIALIAS)))
            self.image = img.image
            IMAGE_LIST.append(img)

    def size_as_tuple(self):
        return self.width, self.height

    def position_as_tuple(self):
        return self.x, self.y


class TileType:
    name = ""
    path = ""
    speed = 1.0

    def by_name(self, name="Dirt"):
        if name.lower().strip() == "dirt" or name.lower().strip() == "d":
            self.name = "Dirt"
            self.path = r"resources/images/dirt.png"
            self.speed = 1.0
        if name.lower().strip() == "concrete" or name.lower().strip() == "c":
            self.name = "Concrete"
            self.path = r"resources/images/concrete.jpg"
            self.speed = 1.0
        return self


class TileImage:
    path = None
    image = None

    def __init__(self, path=None, image=None):
        self.path = path
        self.image = image
