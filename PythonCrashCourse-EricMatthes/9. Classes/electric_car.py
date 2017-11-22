# File: electric_car.py
# Project: python-sandbox
# Local author: kevin
# Created on 11/22/2017 at 12:31 PM
#
# For inquiries about the file please contact the author.

tiy9_9 = '9-9. Battery Upgrade:\nUse the final version of electricCar.py and add a method to the Battery class called ' \
         'upgradeBattery(). This method should check the battery size and set the capacity to 85 if it isn\'t already. ' \
         '\nMake an electric car with a default battery size, call getRange() once, and then call getRange() a second time ' \
         'after upgrading the battery.\n'

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def getDescriptiveName(self):
        longName = '{} {} {}'.format(self.year, self.make, self.model)
        return longName

    def readOdometer(self):
        print('This car has {} miles on it.'.format(self.odometer_reading))

    def updateOdometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def incrementOdometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, batterySize=70):
        """Initialize the battery attributes."""
        self.batterySize = batterySize

    def describeBatter(self):
        """Print a statement describing the battery size."""
        print('This car has a {}-kWh battery.'.format(self.batterySize))

    def getRange(self):
        """Print a statement about the range this battery provides."""
        if self.batterySize == 70:
            range = 240
        elif self.batterySize == 85:
            range = 270
        else:
            range = 200

        print('This car can go approximately {} miles on a full charge.'.format(range))

    def upgradeBattery(self):
        if self.batterySize < 85:
            self.batterySize = 85

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print('This car has a {}-kWh battery.'.format(self.battery.batterySize))

    def fillGasTank(self):
        """Electric cars don't have gas tanks!"""
        print('This car doesn\'t need a gas tank!')


if __name__ == '__main__':
    print('* '*20)
    print(tiy9_9)
    jolt = ElectricCar('honda', 'civic', '2003')  # not an electric car by any means
    jolt.describe_battery()
    jolt.battery.getRange()
    jolt.battery.upgradeBattery()
    jolt.describe_battery()
    jolt.battery.getRange()
