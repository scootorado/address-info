"""
Represents a ward and it's geospatial information.
"""
from shapely.geometry import Point

class Ward:

    def __init__(self, id, multipolygon):
        self.__id = id
        self.__multipolygon = multipolygon

    def contains(self, coordinates):
        return self.__multipolygon.contains(Point(coordinates))

    def id(self):
        return self.__id

    def multipolygon(self):
        return self.__multipolygon