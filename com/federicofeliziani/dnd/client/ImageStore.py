import os

from PIL import Image, ImageTk

from com.federicofeliziani.dnd.client.entities.TileImage import TileImage

RESOURCE_PATH = os.fsencode("resources/images")


class ImageStore:
    IMAGE_LIST = []

    def __init__(self):
        for file in os.listdir(RESOURCE_PATH):
            file_path = os.path.join(RESOURCE_PATH, os.fsencode(file))
            self.IMAGE_LIST.append(TileImage(file, ImageTk.PhotoImage(Image.open(file_path))))

    @staticmethod
    def get_image(name=None, size=None):
        if name is None or len(name.strip()) == 0:
            return None
        for image in ImageStore.IMAGE_LIST:
            if image.path == name:
                ret_img = image
                if size is not None:
                    ret_img.resize(size, Image.ANTIALIAS)
                return ret_img
