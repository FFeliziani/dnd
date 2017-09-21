from com.federicofeliziani.dnd.client.ImageStore import ImageStore
from com.federicofeliziani.dnd.client.entities.Rect import Rect
from com.federicofeliziani.dnd.client.entities.TileType import TileType

IMAGE_LIST = []


class Tile(Rect):
    idx = 0
    idy = 0
    type = None
    image = None
    id = -1

    def __init__(self, x=None, y=None, position=None, width=None, height=None, size=None, tile_type="Dirt", index=None):
        if position is None and x is not None and y is not None:
            self.idx = x
            self.idy = y
        if position is not None and x is None and y is None:
            self.idx = position.x
            self.idy = position.y
        if x is None and y is None and position is None:
            self.idx = 0
            self.idy = 0
        if size is None and width is not None and height is not None:
            self.width = width
            self.height = height
        if width is None and height is None and size is not None:
            self.width = size.width
            self.height = size.height
        if self.idx is not None and self.idy is not None and self.width is not None and self.height is not None:
            self.x = self.idx * self.width
            self.y = self.idy * self.height
        if width is None and height is None and size is None:
            self.width = 0
            self.height = 0
        self.type = TileType.by_name(TileType(), name=tile_type)
        self.image = ImageStore.get_image(self.type.path)
        # found = False
        # for img in IMAGE_LIST:
        #     if img.path == self.type.path:
        #         self.image = img.image
        #         found = True
        # if not found:
        #     img = TileImage(path=self.type.path, image=ImageTk.PhotoImage(Image.open(self.type.path).resize(self.size_as_tuple(), Image.ANTIALIAS)))
        #     self.image = img.image
        #     IMAGE_LIST.append(img)
