"""
Given an address, provides geo-location coordinates.  This uses the https://geocoding.geo.census.gov/
data API to help with the translation.

See the document Geocoding_Services_API.pdf at https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.pdf
or the version included in this project.
"""
import requests, melog


def get_geo_location(config, address):
    parameters = {'street': address.street(), 'city': address.city(), 'state': address.state(), 'zip': address.zip(),
                  'benchmark': __BENCHMARK, 'format': __FORMAT}

    r = requests.get(config.geo_service_url, params=parameters)
    r_dict = r.json()

    if r_dict['result'] and r_dict.get('result')['addressMatches']:
        address_matches = r_dict.get('result').get('addressMatches')
        if len(address_matches) > 1:
            melog.error("Found more than one address matches.  address=%s", address)
            exit(1)

        address_match = address_matches[0]
        if address_match['coordinates']:
            coordinates = address_match.get('coordinates')
            return coordinates

    melog.error('Unable to find coordinates for address.  address=%s', address)
    exit(1)


__BENCHMARK = '4'  # Public_AR_Current
__FORMAT = 'json'
