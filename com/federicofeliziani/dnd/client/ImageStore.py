import os

from PIL import Image

from com.federicofeliziani.dnd.client.entities.TileImage import TileImage

RESOURCE_PATH = os.fsencode("resources/images")


class ImageStore:
    IMAGE_LIST = []

    def __init__(self):
        for file in os.listdir(RESOURCE_PATH):
            file_path = os.path.join(RESOURCE_PATH, os.fsencode(file))
            self.IMAGE_LIST.append(TileImage(path=file, image=Image.open(file_path)))

    @staticmethod
    def get_image(name=None, size=None):
        if name is None or len(name.strip()) == 0:
            return None
        for image in ImageStore.IMAGE_LIST:
            if size is not None and image.path == "{0}_{1}x{2}".format(name, size[0], size[1]).encode():
                return image
            if size is not None and image.path == name:
                ret_img = image
                ret_img.resize(size=size)
                ImageStore.IMAGE_LIST.insert(0, TileImage(path="{0}_{1}x{2}".format(name, size[0], size[1]).encode(), image=ret_img.image))
                return ret_img
            if size is None and image.path == name:
                return image
        return None
