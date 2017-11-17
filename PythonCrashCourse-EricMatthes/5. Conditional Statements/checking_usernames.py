# File: checking_usernames
# Project: python-sandbox
# Local author: kevin
# Created on 09/30/2017 at 3:15 PM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* '*20)
tiy5_10 = "5-10. Checking Usernames.\nDo the following to create a program that simulates how websites ensure that everyone has a unique username."
tasklist = ["Make a list of five or more usernames called 'current_users'."
            ,"Make another list of five usernames called 'new_users'. Make sure one or two of the new usernames "
             "are also in the 'current_users' list."
            ,"Loop through 'new_users' to see if each new username has already been used."]
print(tiy5_10)
for n,task in enumerate(tasklist,1):
    print("Task " + str(n)+ ":\t" + task)

# BEGIN SOLUTION
current_users = ["guest", "admin", "kevin", "config", "remote"]
current_users_lower = [e.lower() for e in current_users]
new_users = ["kevin", "apple", "pear", "admin", "banana"]
new_users_lower = [e.lower() for e in new_users]

print('\n')
for i,e in enumerate(new_users): #index, element
    temp = e
    print("Registering " + e + " as a new user...")
    while temp.lower() in current_users_lower:
        newUser = raw_input("\nThere is already a user with this name. Please provide another username: ")
        if (newUser.lower() not in new_users):
            print("Deleting " + temp + " and registering " + newUser + " as a new user...")
            temp = newUser
            new_users.remove(e)
            new_users.insert(i, newUser)
            print ("The queue for new users registration is now as follows:"),
            for e in new_users[:-1]:
                print e + ",",
            print (new_users[-1] + '\n')
        else:
            print("The new user you have entered is already queued for registration.")

# END SOLUTION
