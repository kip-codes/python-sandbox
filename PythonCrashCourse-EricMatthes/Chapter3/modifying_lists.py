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


# Assignment prompt
print('\n')
print('* ' * 20)
tiy3_6 = "You just found a bigger dinner table, so now more space is available. " \
         "Think of three more guests to invite to dinner.\n"
print("3-6. More Guests:\n" + tiy3_6)

# copy list from 3-4
guests = ["Abraham Lincoln, Vampire Slayer","Oprah Winfrey","Joan of Arc"]

# add a guest at the beginning of the list
guests.insert(0, "Barefoot Contessa")

# add a guest to the middle of the list
guests.insert(len(guests)/2, "Princess Leia")

# add a guest to the end of the list
guests.append("Paula Dean")

rsvp_0 = guests[0] + ", my gratitudes for being such a wondrous companion. Please come to my dinner next morrow!"
rsvp_1 = "How are the book sales going, " + guests[1] + "? Tell me about it over dinner sometime!"
rsvp_2 = "Let's catch up -- are you free tomorrow, " + guests[2] + "?"
rsvp_3 = "Hey " + guests[3] + "! Let's get brunch some time with the gals."
rsvp_4 = "It's been a while since we've gone for coffee... are you free this Sunday, " + guests[4] + "?"
rsvp_5 = "You. Me. Eat. 3:00pm tomorrow, " + guests[5] + "-- be there or be square."
msgs = [rsvp_0, rsvp_1, rsvp_2, rsvp_3, rsvp_4, rsvp_5]

# print all invitations
for msg in msgs:
    print msg


# Assignment prompt
print('\n')
print('* ' * 20)
tiy3_7 = "You just found out that your new dinner table won't arrive in time for the dinner, and you have space for " \
         "only two guests."
print("3-7. Shrinking Guest List:\n" + tiy3_7 + '\n')

# begin solution

# copy list from 3-6
guests = ["Abraham Lincoln, Vampire Slayer","Oprah Winfrey","Joan of Arc"]
guests.insert(0, "Barefoot Contessa")
guests.insert(len(guests)/2, "Princess Leia")
guests.append("Paula Dean")
rsvp_0 = guests[0] + ", my gratitudes for being such a wondrous companion. Please come to my dinner next morrow!"
rsvp_1 = "How are the book sales going, " + guests[1] + "? Tell me about it over dinner sometime!"
rsvp_2 = "Let's catch up -- are you free tomorrow, " + guests[2] + "?"
rsvp_3 = "Hey " + guests[3] + "! Let's get brunch some time with the gals."
rsvp_4 = "It's been a while since we've gone for coffee... are you free this Sunday, " + guests[4] + "?"
rsvp_5 = "You. Me. Eat. 3:00pm tomorrow, " + guests[5] + "-- be there or be square."
msgs = [rsvp_0, rsvp_1, rsvp_2, rsvp_3, rsvp_4, rsvp_5]

notice = "Sorry y'all, I miscounted. You have to battle to the death to get the two spots actually available."
print(notice)

# remove guests from list one at a time
n = len(guests)
while n > 2:
    print("Sorry " + guests[-1] + ", I cannot invite you to the dinner. Goodbye.")
    guests.pop()
    n = n-1

for x in guests:
    print("Congratulations, " + x + "! You're still in the running to eat dinner with me.")

## Remove all guests
# print(guests)
for n in range(len(guests)):
    del guests[0]

# del guests <-- would delete the entire data structure instead of the elements only

print(guests)



# end solution