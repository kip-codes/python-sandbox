# File: no_users
# Project: python-sandbox
# Local author: kevin
# Created on 09/30/2017 at 2:06 PM
#
# For inquiries about the file please contact the author.
print('* ' * 20)
tiy5_9 = "5-9. No Users:\nAdd an if test to 'hello_admin.py' to make sure the list of users is not empty."
tasklist = ["If the list is empty, print the message 'We need to find some users!'"
            ,"Remove all of the usernames from your list, and make sure the correct message is printed."]
print(tiy5_9)
for n,task in enumerate(tasklist,1):
    print("Task " + str(n)+ ":\t" + task)

# BEGIN SOLUTION
# copying program from hello_admin.py
users = ['junglejim4288', 'local', 'guest', 'admin', 'kevin']
print("\nTesting for empty list...")

if users:
    removeChoice = raw_input("There seem to be some unused users on this account. Would you like me to remove them? (y/n) ")
    if(removeChoice.lower() == "y" or removeChoice.lower() == "yes"):
        del users[:]
        if (not users):
            print("users is now empty.")
            print type(users)
    else:
        print("Ok, exiting the program.")
else:
    noUsersMsg = "There are no users on this account. In the next program, we'll add some users!"
    print(noUsersMsg)

# END SOLUTION