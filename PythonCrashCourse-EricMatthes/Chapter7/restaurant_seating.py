# File: restaurant_seating
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 10/16/2017 at 5:42 PM
#
# For inquiries about the file please contact the author.

print('* ' * 20)
tiy7_2 = "7-2. Restaurant Seating:\nWrite a program that asks the user how many people are in their dinner group. " \
         "If the answer is more than what is available, print a message saying they'll have to wait for a table." \
         "\nOtherwise, report that their table is ready."
print(tiy7_2)

print("= = = = =\nTo make things more interesting I will make restaurant capacity static, but available seats dynamic."
      "\nThat is, tables will become available after some time."
      "\nThis will require multi-threading, which will be a first for me!")

print("In this scenario, we assume that the restaurant is fully automated and encourages self-service."
      "\nThe program provides a means of organizing the chaos behind the automation by directing customers to an "
      "appropriate table.")

# BEGIN SOLUTION
import time, threading

# ERROR CODES
# 1: success
# 2: prompt the user for another choice
# 0: exit program


def hello():
    print("hello, Timer")

# checkSeats(): Check how many seats at a table are ready for a customer.
def checkSeats(partySize, name, locPref):
    global tables  # this allows access to the tables variable defined in main

    for t in tables:
        # If the customer requires a specific seat
        if tables[t]['location'] == locPref:  # access the preferred location
            if tables[t]['seated'] == 0 and tables[t]['ready'] >= partySize: # a table is cleaned and prepared for a customer
                print("Alright " + name.title() + ", our table is ready for you. Please follow me.")
                return t
    # If nothing is available for them
    if locPref != 'any':
        print("I'm sorry " + name.title() + ", but our tables in the " + locPref + " are currently occupied.")
        return 2
    else:  # locPref is any
        print("Please try again, there are no tables at all!")
        return 2


if __name__ == '__main__':
    # t = threading.Timer(3.0, hello)
    # t.start()

    # First, let's establish a dictionary of tables and presumed placements within the restaurant.
    # ready: seats that are ready for a customer (assume ready is fixed)
    # seated: seats currently occupied by a customer (cannot exceed ready)
    tables = {
        "1a": {"ready": 2, "seated": 0, "location": "bar"},
        "1b": {"ready": 2, "seated": 0, "location": "bar"},
        "1c": {"ready": 2, "seated": 0, "location": "bar"},
        "2a": {"ready": 5, "seated": 0, "location": "lounge"},
        "2b": {"ready": 4, "seated": 0, "location": "lounge"},
        "2c": {"ready": 6, "seated": 0, "location": "lounge"},
        "3a": {"ready": 10, "seated": 0, "location": "mezzanine"},
        "3b": {"ready": 12, "seated": 0, "location": "mezzanine"}
    }

    print('\n\n')
    name = str(input("Good evening, what is your name: "))
    partySize = int(input("Thank you, " + name.title() + ". And how big is your party: "))
    preference = str(input("And where would you like to be seated tonight? You can enter 'any' if you do not have a "
                       "preference: "))

    checkSeats(partySize,name,preference)