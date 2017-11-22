# File: icecreamshop
# Project: python-sandbox
# Local author: kevin
# Created on 11/21/2017 at 7:04 PM
#
# For inquiries about the file please contact the author.

import restaurant


class IceCreamStand(restaurant.Restaurant):
    """Represents aspects of an ice cream stand, stemmed from the Restaurant type."""
    def __init__(self, restaurantName, cuisineType):
        """Initialize attributes of the parent class.
        Then, initialize attributes specific to an ice cream stand."""
        super().__init__(restaurantName, cuisineType)
        self.flavors = []

    def checkFlavors(self):
        """Prints list of flavors stored in attribute of the ice cream stand."""
        pass

    def changeFlavors(self):
        """Modifies the list of flavors available at the ice cream stand."""
        pass

    def addFlavor(self, *flavors):
        """Adds one or more flavors to the ice cream stand."""
        pass

    def removeFlavor(self, *flavors):
        """"Deletes one or more flavors from the ice cream stand."""
        pass


if __name__ == '__main__':
    pass

