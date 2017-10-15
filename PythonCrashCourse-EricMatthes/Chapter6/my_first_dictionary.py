# File: my_first_dictionary
# Project: python-sandbox
# Local author: kevin
# Created on 09/30/2017 at 4:23 PM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* ' * 20)
tiy6_1 = "6-1. Person:\nUse a dictionary to store information about a person you know." \
         " Store their first name, last name, age, and the city in which they live." \
         "\nPrint each piece of information stored in your dictionary."
print tiy6_1

# BEGIN SOLUTION
famous_person = {
    "first_name": "Barefoot",
    "last_name": "Contessa",
    "age": "timeless",
    "city": "Chicago"
}
for x in famous_person:
    print ("This person's " + x + " is " + famous_person[x])
# END SOLUTION

# Assignment prompt
print ('* ' * 20)
tiy6_2 = "6-2. Favorite Numbers:\nUse a dictionary to store people's favorite numbers.\nThink of five names, and use" \
         " them as keys in your dictionary.\nThink of a favorite number for each person, and store them as keys in the" \
         " dictionary.\nPrint each person's name and their favorite number."
print tiy6_2

# BEGIN SOLUTION
print '\n'
fave_nums = {
    "Shea Coulee": 3,
    "Sasha Velour": 1,
    "Nina Bo'Nina Brown": 666,
    "Trixie Mattel": 10,
    "Evah Destruction": 11
}
for x in fave_nums:
    print (x + "'s favorite number is " + str(fave_nums[x]))
# END SOLUTION