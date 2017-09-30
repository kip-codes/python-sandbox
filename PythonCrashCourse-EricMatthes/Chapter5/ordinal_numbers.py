# File: ordinal_numbers
# Project: python-sandbox
# Local author: kevin
# Created on 09/30/2017 at 4:10 PM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* ' * 20)
tiy5_11 = "5-11. Ordinal Numbers:\nOrdinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in -th," \
          " except 1, 2 and 3."
tasklist = ["Store the numbers 1 through 9 in a list."
            ,"Loop through the list."
            ,"User an if-elif-else chain inside the loop to print the proper ordinal ending for each number."
             " Each output should be on a separate line."]
print(tiy5_11)
for n,task in enumerate(tasklist,1):
    print("Task " + str(n)+ ":\t" + task)

# BEGIN SOLUTION
print('\n')
digits = [x for x in range(1,10)]
for e in digits:
    if (e == 1):
        print (str(e) + "st")
    elif (e == 2):
        print (str(e) + "nd")
    elif (e == 3):
        print (str(e) + "rd")
    else:
        print(str(e) + "th")

# END SOLUTION