# File: modifying_lists
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 09/23/2017 at 8:56 PM
#
# For inquiries about the file please contact the author.
import random

# Assignment prompt
print('* ' * 20)

tiy3_4 = "If you could invite anyone, living or deceased, to dinner, who would you invite?" \
         "\nMake a list that includes at least three people you'd like to invite to dinner. " \
         "\nThen use your list to print a message to each person, inviting them to dinner. (p. 46)\n"
print("3-4. Guest List:\n" + tiy3_4)

# begin solution
guests = ["Abraham Lincoln, Vampire Slayer","Oprah Winfrey","Joan of Arc"]
rsvp_1 = guests[0] + ", my gratitudes for being such a wondrous companion. Please come to my dinner next morrow!"
rsvp_2 = "How are the book sales going, " + guests[1] + "? Tell me about it over dinner sometime!"
rsvp_3 = "Let's catch up -- are you free tomorrow, " + guests[2] + "?"

print(rsvp_1)
print(rsvp_2)
print(rsvp_3)
# end solution

print('\n')

# Assignment prompt
print('* ' * 20)

tiy3_5 = "You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. " \
         "\nYou'll have to think of someone else to invite." \
         "\nStarting with the program from Exercise 3_4, print the name of the guest who can't make it." \
         "\nModify the list, repalcing the name of the guest who can't make it with the name of the new person you are inviting." \
         "\nPrint a second set of invitation messages, one for each person who is still in your list.\n"
print("3-5. Changing Guest List:\n" + tiy3_5)

# copy list from 3-4
guests = ["Abraham Lincoln, Vampire Slayer","Oprah Winfrey","Joan of Arc"]
rsvp_1 = guests[0] + ", my gratitudes for being such a wondrous companion. Please come to my dinner next morrow!"
rsvp_2 = "How are the book sales going, " + guests[1] + "? Tell me about it over dinner sometime!"
rsvp_3 = "Let's catch up -- are you free tomorrow, " + guests[2] + "?"
msgs = [rsvp_1, rsvp_2, rsvp_3]

x = random.randint(0,len(guests)-1) # random index
y = random.choice(guests) # cleaner way to select random element from list
print("Unfortunately, " + y + " has just informed us that they are unable to attend the party."
      "\nLet's find someone else to take their spot.")

# first, remove the invitation for that guest.
i = guests.index(y)
msgs.pop(i) # indexing will be messed up, but this is good to experiment with

# delete the guest from the list
guests.remove(y)

print("\nThe intermediate guest list is now:")
for i in guests:
    print(i)

print('\n')

newGuest = "DJ Khaled"
guests.append(newGuest)

newMsg = guests[-1] + ", I'm so glad you're here. Come to my dinner."
msgs.append(newMsg)

for m in msgs:
    print m
# end solution