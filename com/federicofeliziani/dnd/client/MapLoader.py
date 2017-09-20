import os
import json

from com.federicofeliziani.dnd.client.entities.Map import Map
from com.federicofeliziani.dnd.client.entities.Tile import Tile

BASE_MAP_PATH = r"resources\maps"


class MapLoader:
    @staticmethod
    def load(map_name="map1"):
        if map_name is not None:
            map_file = None
            with open(os.path.join(BASE_MAP_PATH, map_name), "r") as f:
                map_file = json.loads(f.read())
            return_map = Map()
            return_map.height = map_file["height"]
            return_map.width = map_file["width"]
            return_map.data = map_file["data"]
            return_map.map_name = map_file["name"]
            return_map.tiles = MapLoader.tiles_from_data(return_map)
        return return_map

    @staticmethod
    def tiles_from_data(the_map=None):
        if the_map is not None:
            tiles = []
            for idx, t in enumerate(the_map.data):
                tile = Tile(tile_type=t, x=idx % the_map.width, y=int(idx / the_map.height), height=100, width=100)
                tiles.append(tile)
            return tiles
