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
        if len(self.flavors) == 0:
            print("Sorry -- {rn} doesn't seem to sell any flavors at the moment.".format(rn=self.restaurantName))
            return
        print("{rn} sells these flavors:".format(rn=self.restaurantName))
        for flavor in self.flavors:
            print("-\t" + flavor)

    def changeFlavors(self):
        """Modifies the list of flavors available at the ice cream stand."""
        while True:
            try:
                prompt = "What would you like to do:" \
                    "\n\t1. Add a flavor to the menu." \
                    "\n\t2. Delete a flavor from the menu." \
                    "\nEnter a number to select a choice." \
                    "\n>> "
                choice = int(input(prompt))
                if choice <= 0:
                    raise ValueError()
            except ValueError:
                print("Unacceptable choice. The input must be a digit without any trailing characters.")
            else:  # valid choice
                if choice == 1:
                    self.addFlavor(self.takeFlavor(choice))
                    break
                elif choice == 2:
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
            print(str(count)+".\t")
            flavor = input()
            if flavor == 'q':
                break
            flavors.append(flavor)
            count += 1  # Tracks the number of entries taken so far

        print("You have entered:")
        for flavor, n in enumerate(flavors, 1):
            print(n + ".\t" + flavor)

        while True:
            c = input("\nAre you satisfied with this selection? (y/n)").lower()
            if c == 'y' or c == 'yes':
                return flavors
            elif c == 'n' or c == 'no':
                return []  # Returns an empty list so nothing gets modified
            else:  # invalid entry
                print("\nPlease enter yes or no.")

    def addFlavor(self, *flavors):
        """Adds one or more flavors to the ice cream stand."""
        print("\nAdding the following items to the menu...")
        for flavor in flavors:
            print("+\t"+flavor)
            if flavor not in self.flavors:
                self.flavors.append(flavor)
            else:  # flavor already exists on menu
                print("\nThe flavor you would like to add is already on the menu, skipping over...")

    def removeFlavor(self, *flavors):
        """"Deletes one or more flavors from the ice cream stand."""
        print("\nDeleting the following items from the menu...")
        for flavor in flavors:
            print("-\t"+flavor)
            if flavor in self.flavors:
                self.flavors.remove(flavor)
            else:  # flavor is not in attribute0
                print("\nThe flavor to be removed is not sold at {rn}, skipping over...".format(rn=self.restaurantName))

    def mainMenu(self):
        print("Hello ADMIN! You've selected a restaurant. What would you like to do?")
        options = [
            '\n1. Information about the selected restaurant.'
            '\n2. Open the restaurant for business.'
            '\n3. Close the restaurant for the day.'
            '\n4. Establish'
        ]


if __name__ == '__main__':
    twoScoops = IceCreamStand('Two Scoops', 'ice cream')
    twoScoops.mainMenu()


