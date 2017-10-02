# File: favorite_languages
# Project: python-sandbox
# Local author: kevin
# Created on 09/30/2017 at 4:59 PM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* ' * 20)
tiy6_6 = "6-6. Polling:\nUse the code in 'favorite_languages.py' (p. 104)."
tasklist = ["Make a list of people who should take the favorite languages poll. Include some names that are already"
            " in the dictionary and some that are not."
            ,"Loop through the list of people who should take the poll. If they have already taken the poll,"
             " print a message thanking them for responding. If they have not yet taken the poll, prompt them to."]
print tiy6_6
for i,x in enumerate(tasklist,1):
    print ("Task " + str(i) + ": " + str(x))

# BEGIN SOLUTION
favorite_languages = {
    "Barefoot Contessa": "\'The food is imported from Italy\'",
    "Bobby Flay": "cuisine",
    "Jeff Kaplan": "C++",
    "Fabio": "love",
    "Jim Gaffigan": "comedy"
}
poll_prospects = {
    "Michael Cera": 0,
    "Queen Latifah": 0,
    "Ellen Degeneres": 0,
    "Bobby Flay": 0,
    "Jim Gaffigan": 0
}

for x in poll_prospects:
    if x in favorite_languages:
        poll_prospects[x] = 1 # Marks the prospect as cleared
        print('\n' + x + ", thank you for telling us your favorite language is " + favorite_languages[x] + ".")
    else:
        print('\n' + x + ", we care about you as a client and would like to know more about you!")
        newLanguage = raw_input("In the space allotted below, please tell us what your favorite language is.\n")
        favorite_languages.update({x:newLanguage})
        poll_prospects[x] = 1
        print("Thank you for telling us! Your new default language is " + favorite_languages[x] + ".")


# check if poll prospects have been followed up on
if all(set(poll_prospects.values())) == 0:
    print("\nIt appears we are missing a few prospects.")
else:
    print('= ' * 5 + "\nAll prospects have been followed up on. Congratulations!")

# review poll results
for x in favorite_languages:
    print("We have recorded that " + x + "'s favorite language is " + favorite_languages[x] + ".")

# program exit statement
print("End of client list reached. See director for next step.")

# END SOLUTION