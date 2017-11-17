# File: conditionals
# Project: PythonCrashCourse
# Local author: kevin
# Created on 09/28/2017 at 1:29 PM
#
# For inquiries about the file please contact the author.
import random


# Assignment prompt
print('* ' * 20)
tiy5_1 = "5-1. Conditional Tests:\nWrite a series of conditional tests. Prince a statement describing each test and your prediction for " \
         "the result of each test.\nCreate at least 10 tests, with at least 5 evaluating to True and rest to false.\n"
print(tiy5_1)


# begin solution
rnums = [random.randint(1,10) for n in range(10)]
print("rnums is " + str(rnums))

gtcount = 0

for x in rnums:
    if x >= 5:
        gtcount += 1
        print("gte+", gtcount)
    else: print("lt+")

print("In this list, we have " + str(gtcount) + " entries greater than or equal to five, and " + str(10-gtcount)
      + " less than five.")
# end solution


# Assignment prompt
print('* ' * 20)
tasklist = ["Tests for equality and inequality with strings","Tests using the lower() function",
            "Numerical tests involving equality and inequality","Tests using the and keyword and the or keyword",
            "Test whether an item is in a list","Test whether an item is not in a list"]
tiy5_2 = "5-2. More Conditional Tests:\nHave at least one True and one False result for each of the following:\n"
print(tiy5_2)
for n,task in enumerate(tasklist,1):
    print("Task " + str(n)+ ":\t" + task)

# begin solution
print("\nTesting for Task 1...")
msg = "Hello world!"
print("msg is " + msg)
print("Is msg, 'Hello planet?")
if msg == "Hello planet":
    print("Yes it is!")
else:
    print("Unfortunately, no it is not.")


print("\nTesting for Task 2...")
msg = "Merry Christmas"
print("msg is " + msg)
print(msg.lower() == "merry christmas")

print("\nTesting for Task 3...")
digit = 4
print("digit is " + str(digit))
print(digit >= 3)

print("\nTesting for Task 4...")
result = 70
print("result is " + str(result))
print(result >= 10 and result < 40 or result > 40)

print ("\nJoint testing for Task 5 & 6...")
myList = [4, 5, 10]
print("myList is"),
for x in myList[:-1]:
    print(x),
print myList[-1]
# Testing list contents
print "Is Mayonnaise in the list:","Mayonnaise" in myList
print "How about 6? Is 6 in the list:",6 in myList
print "...5? That should be in the list:",5 in myList

# end solution