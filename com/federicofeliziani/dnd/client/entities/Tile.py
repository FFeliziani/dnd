class Tile:
    x = 0
    y = 0
    width = 0
    height = 0
    type = None

    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class TileType:
    name = ""
    path = ""

    def __init__(self, name="Dirt", path="resources/images/dirt.png"):
        self.name = name
        self.path = path