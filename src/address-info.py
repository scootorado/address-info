#!/usr/bin/env python

import arguments, melog, geoloc
from config import Config
from address import Address


if __name__ == '__main__':

    melog.info("starting address-info application")

    options, arguments = arguments.get_args()
    config = Config()

    my_address = Address(options.address)

    coordinates = geoloc.get_geo_location(config, my_address)

    print(coordinates)
