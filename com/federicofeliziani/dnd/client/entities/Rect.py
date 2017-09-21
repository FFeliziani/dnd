class Rect:
    x = 0
    y = 0
    width = 0
    height = 0

    def size_as_tuple(self):
        return self.width, self.height

    def position_as_tuple(self):
        return self.x, self.y
