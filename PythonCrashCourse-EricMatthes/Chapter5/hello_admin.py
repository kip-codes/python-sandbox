# File: hello_admin
# Project: python-sandbox
# Local author: kevin
# Created on 09/30/2017 at 1:55 PM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* ' * 20)
tiy5_8 = "5-8. Hello Admin:\nMake a list of five or more usernames, including the name 'admin'." \
         " Imagine you are writing code that will print a greeting to each user after they log in to a website." \
         " Loop through the list, and print a greeting to each user."
tasklist = ["If the username is 'admin', print a special greeting. Otherwise, print a generic greeting."]
print(tiy5_8)
for n,task in enumerate(tasklist,1):
    print("Task " + str(n)+ ":\t" + task)

# BEGIN SOLUTION
users = ['junglejim4288', 'local', 'guest', 'admin', 'kevin']
for x in users:
    if (x == "admin"):
        print("Hello " + x + ", would you like to see a status report?")
    else:
        print("Hello " + x + ", thank you for logging in again.")

# END SOLUTION
