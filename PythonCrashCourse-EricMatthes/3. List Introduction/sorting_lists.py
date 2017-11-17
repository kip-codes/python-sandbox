# File: sorting_lists
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 09/24/2017 at 12:00 AM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* ' * 20)
tiy3_8 = "Think of at least five places in the world you'd like to visit. " \
         "\nStore the locations in a list, making sure they are not in alpha-order. " \
         "\nComplete the permanent and temporary sorting objectives. (p. 50)"
print("3-8: Seeing the World:\n" + tiy3_8)

## BEGIN solution 3-8
# Store the locations in a list
places = ["Spain", "Sweden", "Denmark", "Brazil", "South Korea"]

# Print list in original order, then sorted (temporarily).
print("\nOriginal list:")
print(places)

print("\nTemporarily sorted list, using sorted():")
print(sorted(places))

print("\nHere is the original variable:")
print(places)

print("\nTemporarily sorted list in reverse, using sorted():")
print(sorted(places, reverse=True))

print("\nHere is the original variable:")
print(places)

print("\nReversing the list permanently...")
places.reverse()
print(places)

print("\nReversing the reversed list...")
places.reverse()
print(places)

print("\nSorting the list permanently...")
places.sort()
print(places)

print("\nSorting the list in reverse alphabetical order...")
places.sort(reverse=True)
print(places)

## END solution 3-8

# Assignment prompt
print("\n")
print('* ' * 20)
tiy3_9 = "Working with one of the programs from Exercises 3-4 through 3-7, use len() to print a message " \
         "indicating the number of people you are inviting to dinner."
print("3-9. Dinner Guests:\n" + tiy3_9)

## BEGIN solution

# Use program from Exercise 3-4
guests = ["Abraham Lincoln, Vampire Slayer","Oprah Winfrey","Joan of Arc"]

print('\n')
print(guests)
print("At tonight's dinner, there will be " + str(len(guests)+1) + " guests, including myself.")

## END solution

# Assignment prompt
print('\n')
print('* ' * 20)
tiy3_10 = "Think of something you could store in a list." \
          "\nWrite a program that creates a list containing these items and then uses each function introduced in his chapter at least once."
print("3-10. Every Function:\n" + tiy3_10)

colors = ["Green","Blue","Red","Violet","Black"]
print(colors)
print(sorted(colors))
print(sorted(colors,reverse=True))

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

for x in colors:
    print x

colors.append('Beige')
colors.pop(3)

print(colors)