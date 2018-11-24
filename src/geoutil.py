"""
Responsible for loading geospatial data into the Shapely libraries.
"""
import json, melog
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from ward import Ward

def load_ward_geospatial_data():
    f = open('boundaries-wards-geo-2015.json', 'r')
    ward_geo_dict = json.load(f)

    ward_list = []
    for feature in ward_geo_dict.get('features'):
        ward_id = feature.get('properties').get('ward')
        coordinates_level_1 = feature.get('geometry').get('coordinates')

        polygons = []
        for coordinates_level_2 in coordinates_level_1:
            for coordinates_level_3 in coordinates_level_2:
                polygon = __generate_polygon(ward_id, coordinates_level_3)
                if polygon:
                    polygons.append(polygon)

        multipolygon = MultiPolygon(polygons)
        ward_list.append(Ward(ward_id, multipolygon))

    return ward_list


def __generate_polygon(ward_id, coordinates_list):
    if len(coordinates_list) <= 1:
        melog.error("Expected coordinates at this point but found none.  ward_id=%s", ward_id)
        exit(1)

    coordinates_tuple = []
    for coordinates in coordinates_list:
        coordinates_tuple.append((coordinates[0], coordinates[1]))

    return Polygon(coordinates_tuple)
