# File: my_first_list
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 09/23/2017 at 7:15 PM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print("3-1. Store the names of a few of your friends in a list called 'names'.\n"
      "Print each person's name by accessing each element in the list, one at a time. (p. 40)")

# begin solution 3-1
friends = ['Bob', "Billy", "Michelle Jacobson"]

for i in friends:
    print i
### end solution 3-1

print("\n")

# Assignment prompt
print("3-2. Start with the list you used in Exercise 3-1, but instead of just printing each person's name, "
      "print a message to them.\nThe text of each message should be the same, but each message should be personalized "
      "with the person's name")

# begin solution 3-2
friends = ["Bob","Billy","Michelle Jacobson McDonalds"]
message = "I was told by AppleCare"
for i in friends:
    print(message + ", " + i + ".")
#### end solution 3-2

print('\n')

# Assignment prompt
print("3-3. Think of your favorite mode of transportation, and make a list that stores several examples. Make sentences "
      "by indexing the list.")

#begin solution 3-3
unitrans = ["A","Z","M"]

print("Those interested in going to the Quad of the UC Davis campus should take the " + unitrans[0] + " line.")
print("Trying to go to Target? Take the " + unitrans[1] + " line!")
print("Or, if you're just trying to get anywhere, take the " + unitrans[2] + " line.")
#end solution 3-3