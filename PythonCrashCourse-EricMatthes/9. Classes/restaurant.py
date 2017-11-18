# File: restaurant
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 11/17/2017 at 4:05 PM
#
# For inquiries about the file please contact the author.
import time

def getPrompt():
    tiy9_1 = '\n9-1. Restaurant:\nMake a class called Restaurant. The __init__() method for this class should store two ' \
             'attributes: a restaurant name and a cuisine type.\nMake an instance called restaurant from your class. ' \
             'Print the two attributes individually, and then call both methods.\n'
    print('* ' * 20, tiy9_1)

class Restaurant():
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurantName, cuisineType):
        """Initialize restaurant name and cuisine attributes."""
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        self.open = False
        self.timeOpened = 0

    def describeRestaurant(self):
        """"Prints attributes of restaurant."""
        print('The restaurant is called {}.'.format(self.restaurantName.title()))
        print('At {name}, they serve {cuisine}.'.format(name=self.restaurantName.title(), cuisine=self.cuisineType.lower()))

    def openRestaurant(self):
        """Opens the restaurant to customers."""
        if self.open == False:
            self.open = True
            print('The restaurant is now open!')
            self.timeOpened = time.time()
        else:
            newTime = time.time()
            print('The restaurant has been already open to customers for {:.0f} seconds.'.format(
                newTime - self.timeOpened))
            self.timeOpened = newTime

    def closeRestaurant(self):
        """Closes the restaurant to customers."""
        if self.open == False:
            print('The restaurant has already been closed. Use openRestaurant() when you are ready for business.')
        else:
            self.open = False
            print('The restaurant is now closed. See you tomorrow!')



if __name__ == '__main__':
    getPrompt()

    restaurant = Restaurant('Chik N\' Fries', 'Fried foods')
    print(restaurant.restaurantName, restaurant.cuisineType, '\n')

    restaurant.describeRestaurant()
    time.sleep(1)

    print('\n(Opening the restaurant...)')
    restaurant.openRestaurant()
    print('(Sleeping program for 5 seconds...)')
    time.sleep(5)

    print('\n(When trying to open a restaurant that is already open...)')
    restaurant.openRestaurant()
    time.sleep(1)

    print('\n(Closing the restaurant...)')
    restaurant.closeRestaurant()
    time.sleep(1)

    print('\n(When trying to close a restaurant that is already closed...)')
    restaurant.closeRestaurant()

    veganRestaurant = Restaurant('Leaf Me Pea', 'Grass')
    print('\n(Creating a vegan restaurant...)')
    time.sleep(1)
    veganRestaurant.describeRestaurant()

    scamRestaurant = Restaurant('Nigerian Prince', 'Identify Theft')
    print('\n(Creating a fake restaurant...)')
    time.sleep(1)
    scamRestaurant.describeRestaurant()
