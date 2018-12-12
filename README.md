# address-info

This project will match up an address to the ward it is in using geospatial information from the City of Chicago.

This program will get the address from an excel spreadsheet.  Then, make a REST call to get the geolocation of the
address.  The geolocation information will be used to determine which ward the address is in based on the geospatial
data from the City of Chicago.

## To Run This On The Command Line
- `$ source env/bin/activate`
- `$ python main.py --help`
- `$ python main.py -a "805 S State St, Chicago, IL, 60605"`
- `$ deactivate`

## Additional Information
- [City of Chicago Geographic Information Systems](https://www.cityofchicago.org/city/en/depts/doit/provdrs/gis.html)
- [Chicago Data Portal](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Wards-2015-/sp34-6z76)
- [Geocoding Services API](https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.pdf)

## Geospatial Python Libraries
- [Essential geospatial Python libraries](https://medium.com/@chrieke/essential-geospatial-python-libraries-5d82fcc38731)
- [Shapely](https://shapely.readthedocs.io/en/stable/manual.html)

## Python Packaging and Execution
- [Python to Executable Program](https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263)
- [Python Virtual Environment](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)