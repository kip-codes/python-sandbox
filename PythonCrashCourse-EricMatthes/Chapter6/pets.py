# File: pets
# Project: python-sandbox
# Local author: kevin
# Created on 10/15/2017 at 5:49 PM
#
# For inquiries about the file please contact the author.

print('* ' * 20)
tiy6_8 = "6-8. Pets:\nMake several dictionaries, where the name of each dictionary is the name of a pet. In each " \
         "dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets."
print(tiy6_8)

#BEGIN SOLUTION

pupper = {"name": "pupper", "type": "smol", "owner": "me"}
doggo = {"name": "doggo", "type": "kind of smol", "owner": "me"}
boofer = {"name": "boofer", "type": "not so smol", "owner": "me"}

pets = []
pets.append(pupper)
pets.append(doggo)
pets.append(boofer)

print pets

#Let's present more user-friendly information

for index,x in enumerate(pets,1): #index, element
    print(str(index) + ": " + x["name"].title())
    print("\tType: " + x["type"].title())
    print("\tOwner: " + x["owner"].title())

#END SOLUTION