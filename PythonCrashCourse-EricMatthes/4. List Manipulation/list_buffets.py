# File: list_buffets
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 09/24/2017 at 1:52 AM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* ' *20)
tiy4_13 = "A buffet-style restaurant offers only five basic foods. Think of five simple goods, and store them in a tuple." \
          "\nUse a for loop to print each food." \
          "\nTry to modify one of the items and make sure that Python rejects the change." \
          "\nThe restaurant changes its menu, replacing two of the items. Rewrite the tuple and use a for loop to " \
          "print the revised menu.\n"
print("4-13. Buffet:\n" + tiy4_13)

# BEGIN solution
menu = ("mashed potatoes", "salad", "biscuits", "barbeque", "pizza")

for x in menu:
    print x,

new_menu = menu[:-2] # test slicing
print new_menu

new_menu = ("mashed potatoes", "salad", "biscuits", "pasta", "ice cream")
print new_menu
# END solution