"""
Provides a wrapper around configparser to make it more convenient and readable to get configuration values.

When adding configuration values, they must be added to the config.ini file as well as to the code
below.  As a class level variable, in _populate() and __str__().
"""
import configparser, melog, os

class Config:
    geo_service_url = None

    def __init__(self):
        config_path = os.path.dirname(os.path.abspath(__file__)) + '/config.ini'
        melog.info("Using config file %s", config_path)

        self._config = configparser.ConfigParser()
        self._config.read(config_path)
        self.__populate()

        melog.info('%s' % self)

    def __get(self, key):
        return self._config.get('DEFAULT', key)

    def __populate(self):
        self.geo_service_url = self.__get('geo_service_url')


    def __str__(self):
        return "config:\n" \
               "        es_batch_entries=%s\n" % \
               (self.geo_service_url)