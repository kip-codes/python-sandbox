# File: slicing_lists
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 09/24/2017 at 1:34 AM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* ' *20)
print("TiY 4-10. Slices:\n")

toppings = ["mushrooms","sausage","cheese","garlic"]

print("The first three items in the list are:")
print(toppings[:3])

print("The items from the middle of the list are:")
print(toppings[1:-1])

print("The last three items in the list are:")
print(toppings[-3:])


# Assignment prompt
print('\n')
print('* ' *20)
print("TiY 4-11. My Pizzas, Your Pizzas:\n")

friend_toppings = toppings[:]
toppings.append("zucchini")
friend_toppings.append("avocado")

# Prove the lists are different
print("My favorite pizzas are:")
for x in toppings[:-1]:
    print x + ",",
print "and " + toppings[-1] + ".\n"

print("My friend's favorite pizzas are:")
for x in friend_toppings[:-1]:
    print x + ",",
print "and " + friend_toppings[-1] + ".\n"
