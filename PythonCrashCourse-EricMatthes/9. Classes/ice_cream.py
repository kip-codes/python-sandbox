# File: icecreamshop
# Project: python-sandbox
# Local author: kevin
# Created on 11/21/2017 at 7:04 PM
#
# For inquiries about the file please contact the author.

import restaurant, time

tiy9_6 = '9-6. Ice Cream Stand:\nAn ice cream stand is a specific kind of restaurant. Write a class called ' \
         'IceCreamStand that inherits from the Restaurant class.' \
         '\nAdd an attribute called \'flavors\' that stores a list of ice cream flavors. ' \
         'Write a method that displays these flavors.' \
         '\nCreate an instance of IceCreamStand, and call this method.\n'

class IceCreamStand(restaurant.Restaurant):
    """Represents aspects of an ice cream stand, stemmed from the Restaurant type."""
    def __init__(self, restaurantName, cuisineType):
        """Initialize attributes of the parent class.
        Then, initialize attributes specific to an ice cream stand."""
        super().__init__(restaurantName, cuisineType)
        self.flavors = []

    def printFlavors(self):
        """Prints list of flavors stored in attribute of the ice cream stand."""
        if len(self.flavors) == 0:
            print("Sorry -- {rn} doesn't seem to sell any flavors at the moment.".format(rn=self.restaurantName))
            return
        print("{rn} sells these flavors:".format(rn=self.restaurantName))
        for n, flavor in enumerate(self.flavors, 1):
            print(str(n) + ".\t" + flavor)

    def changeFlavors(self):
        """Modifies the list of flavors available at the ice cream stand."""
        while True:
            prompt = "\nWhat would you like to do:" \
                "\n\t1. Add a flavor to the menu." \
                "\n\t2. Delete a flavor from the menu." \
                "\n(Enter 'q' to exit.)"
            print(prompt)
            choice = input('\n>>\t')

            if choice == 'q':
                break
            elif choice == '1':
                self.addFlavor(self.takeFlavor(choice))
                break
            elif choice == '2':
                self.printFlavors()
                if len(self.flavors) > 0:
                    self.removeFlavor(self.takeFlavor(choice))
                break
            else:
                print("Invalid entry.")

    def takeFlavor(self, choice):
        """Takes input from user for adding or removing flavors."""
        if choice == 1:
            prompt = "\nEnter the flavor(s) you would like to add, and enter 'q' when done."
        elif choice == 2:
            prompt = "\nEnter the flavor(s) you would like to remove, and enter 'q' when done."
        else:
            prompt = "MISSING PROMPT"
        print(prompt)
        flavors = []
        count = 1
        while True:
            flavor = input(str(count)+".\t")
            if flavor == 'q':
                break
            flavors.append(flavor)
            count += 1  # Tracks the number of entries taken so far

        print("You have entered:")
        for n, flavor in enumerate(flavors, 1):
            print(str(n) + ".\t" + flavor)

        while True:
            c = input("\nAre you satisfied with this selection? (y/n)\n>>\t").lower()
            if c == 'y' or c == 'yes':
                return flavors
            elif c == 'n' or c == 'no':
                return []  # Returns an empty list so nothing gets modified
            else:  # invalid entry
                print("\nPlease enter yes or no.")

    def addFlavor(self, flavors):
        """Adds one or more flavors to the ice cream stand."""
        if not flavors:
            return

        print("\nAdding the following items to the menu...")
        for flavor in flavors:
            print("+\t"+flavor)
            if flavor not in self.flavors:
                self.flavors.append(flavor)
            else:  # flavor already exists on menu
                print("\nThe flavor you would like to add is already on the menu, skipping over...")

    def removeFlavor(self, flavors):
        """"Deletes one or more flavors from the ice cream stand."""
        print("\nDeleting the following items from the menu...")
        for flavor in flavors:
            print("-\t"+flavor)
            if flavor in self.flavors:
                self.flavors.remove(flavor)
            else:  # flavor is not in attribute0
                print("\nThe flavor to be removed is not sold at {rn}, skipping over...".format(rn=self.restaurantName))

    def mainMenu(self):
        """Prints options for main menu."""
        print("\nHello ADMIN! You've selected a restaurant. What would you like to do?")
        options = [
            '\n1. Information about the selected restaurant.',
            '2. Open the restaurant for business.',
            '3. Close the restaurant for the day.',
            '4. Set how many tables have been waited today.',  # additional options
            '5. Access menu items at the restaurant.',  # additional options
            '(Enter \'q\' to exit.)'
        ]
        for opt in options:
            print(opt)

    def flavorMenu(self):
        """Prints options for accessing or modifying flavors"""
        options = [
            '\n1. Display information about the flavors available.',
            '2. Modify the available flavors.',
            '(Enter \'q\' to exit.)'
        ]
        for opt in options:
            print(opt)

    def flavorMenuNav(self):
        """Allows user to navigate flavors."""
        choice = ''
        while choice != 'q':
            self.flavorMenu()  # print menu
            choice = input('\n>>\t')
            if choice == '1':
                self.printFlavors()
                time.sleep(2)
            elif choice == '2':
                self.changeFlavors()
                time.sleep(2)
            # elif choice == 'q':
            #     break
            else:  # invalid choice
                print('\nInvalid entry. Please enter the digit of the desired option from the list above.')
                time.sleep(3)

    def mainMenuNav(self):
        """Allows user to navigate main menu options. Leads to other options if available."""
        while True:
            self.mainMenu()  # print menu
            choice = input('\n>>\t')
            if choice == 'q':
                print("Thank you, see you soon! Be sure to leave some feedback about your experience in the our"
                      " collection box by the door.")
                break
            elif choice == '1':
                self.describeRestaurant()
                time.sleep(2)
            elif choice == '2':
                self.openRestaurant()
                time.sleep(2)
            elif choice == '3':
                self.closeRestaurant()
                time.sleep(2)
            elif choice == '4':
                self.askTablesServed()
                time.sleep(2)
            elif choice == '5':
                self.flavorMenuNav()
                time.sleep(2)
            else:  # invalid entry
                print('\nInvalid entry. Please enter the digit of the desired option from the list above.')
                time.sleep(3)


if __name__ == '__main__':
    print('* '*20)
    print(tiy9_6)

    twoScoops = IceCreamStand('Two Scoops', 'ice cream')
    twoScoops.mainMenuNav()

