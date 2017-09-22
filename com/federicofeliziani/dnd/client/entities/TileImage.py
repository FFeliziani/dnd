from PIL import Image


class TileImage:
    path = None
    image = None

    def __init__(self, path=None, image=None):
        self.path = path
        self.image = image

    def resize(self, size):
        self.image = self.image.resize(size, Image.ANTIALIAS)
