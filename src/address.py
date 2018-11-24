"""
Provides a class which represents an address
"""

class Address:

    def __init__(self, address):
        """
        :param address:
        """
        self.__address = address

    def __verify_address(self, address):
        return address.split(',').size() == 4

    def street(self):
        return self.__address.split(',')[0]

    def city(self):
        return self.__address.split(',')[1]

    def state(self):
        return self.__address.split(',')[2]

    def zip(self):
        return self.__address.split(',')[3]

    def __str__(self):
        return self.__address