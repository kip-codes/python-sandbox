# File: favorite_places
# Project: python-sandbox
# Local author: kevin
# Created on 10/15/2017 at 6:22 PM
#
# For inquiries about the file please contact the author.

print('* ' * 20)
tiy6_9 = "6-9: Favorite Places\nMake a dictionary called \'favorite_places\'. Think of three names to use as keys in " \
         "the dictionary, and store one to three favorite places for each person." \
         "\nLoop through the dictionary and print each person's name and their favorite place."
print(tiy6_9)

# BEGIN SOLUTION
print('\n')
favorite_places = {
    "billy": ["imagination"],
    "bo": ["farm","park"],
    "bob": ["mall","church","school"]
}

for name in favorite_places: #defaults to keys
    if type(favorite_places.get(name)) is list and len(favorite_places.get(name)) == 1:
        print(name.title() + "\'s favorite place to go is the"),
        for place in favorite_places[name]:
            print(place + ".")
    elif type(favorite_places.get(name)) is list and len(favorite_places.get(name)) > 1:
        print(name.title() + "\'s favorite places to go are the"),
        if len(favorite_places[name]) >= 3:
            for place in favorite_places[name][:-1]:
                print place + ',',
            print("and the " + favorite_places[name][-1] + ".")
        else: # only two elements
            for place in favorite_places[name][:-1]:
                print place,
            print("and the " + favorite_places[name][-1] + ".")
    else: #catch
        print("Something went wrong! Check the type check condition.")

# END SOLUTION