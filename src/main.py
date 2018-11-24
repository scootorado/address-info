#!/usr/bin/env python

import arguments, melog, geoloc, geoutil
from config import Config
from address import Address


if __name__ == '__main__':

    melog.info("starting address-info application")

    options, arguments = arguments.get_args()
    config = Config()

    wards = geoutil.load_ward_geospatial_data()

    my_address = Address(options.address)
    coordinates = geoloc.get_geo_location(config, my_address)

    for ward in wards:
        if ward.contains(coordinates):
            melog.info('address %s is in ward %s', my_address, ward.id())

    melog.info("completed address-info application")
