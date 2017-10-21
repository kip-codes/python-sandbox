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
import time, threading, random

# ERROR CODES
# 1: success
# 2: prompt the user for another choice
# 0: exit program


def hello():
    print("hello, Timer")

# isValidArea(): Checks if user's preference can be accommodated
def isValidArea(locPref):
    global areas

    if locPref == 'any':
        return 0

    if locPref not in areas:
        return 1

def getAreaCap(locPref):
    global areas

    return areas[locPref]

# printRooms(): Print all possible locations in restaurant to sit
def printAllRooms():
    global areas

    for area in areas:
        if len(area) < 9:
            print('\t {}\t\t\t- Seats up to {}'.format(area.title(), areas[area]))
        elif len(area) < 19:
            print('\t {}\t\t- Seats up to {}'.format(area.title(), areas[area]))
        else:
            print('\t {}\t- Seats up to {}'.format(area.title(), areas[area]))


# printLargerRooms(): Prints every room above the party size requirement
def printLargerRooms(partySize):
    global areas

    for area in areas:
        if areas[area] >= partySize:
            if len(area) < 9:
                print('\t {}\t\t\t- Seats up to {}'.format(area.title(), areas[area]))
            elif len(area) < 19:
                print('\t {}\t\t- Seats up to {}'.format(area.title(), areas[area]))
            else:
                print('\t {}\t- Seats up to {}'.format(area.title(), areas[area]))


# printQueuedMsgs(): Prints any message that was stored into a list when waiting for user input. Simulates pop-up msgs.
def printQueuedMsgs():
    global alerts

    if len(alerts) > 1:
        for alert in alerts:
            print(alert)


# takePartySize(): Take input for party size
def takePartySize():
    while True:
        try:
            ps = int(input("\nAnd how big is your party: "))
            if not (ps > 0):
                raise ValueError()
        except ValueError:
            print("Unacceptable party size. Please try again.")
        else:  # success
            print("Ok, party of " + str(ps) + "...")
            break
    return ps


# checkSeats(): Check how many seats at a table are ready for a customer.
def checkSeats(partySize, name, locPref):
    global tables  # this allows access to the tables variable defined in main

    # If the customer's preference will not allow for their party size
    if locPref != 'any' and getAreaCap(locPref) < partySize:
        print("I'm sorry, our tables in the {} cannot seat {} people. Might I recommend you to some areas that can "
              "seat your party?".format(locPref, partySize))
        printLargerRooms(partySize)
        return 2

    if locPref != 'any':  # If the customer requires a specific seat
        for t in tables:
            if tables[t]['location'] == locPref:  # access the preferred location
                if tables[t]['seated'] == 0 and tables[t]['ready'] >= partySize: # a table is cleaned and prepared for a customer
                    print("Alright " + name.title() + ", our table in the " + locPref + " is ready for you.")
                    return t
    else:  # Customer has no preference
        for t in tables:
            if tables[t]['seated'] == 0 and tables[t]['ready'] >= partySize:  # a table is cleaned and prepared for a customer
                print("Alright " + name.title() + ", our table in the " + tables[t]['location'] + " is ready for you.")
                return t

    # If nothing is available for them
    if locPref != 'any':
        print("I'm sorry " + name.title() + ", but our tables in the " + locPref + " are currently occupied.")
        return 2
    else:  # locPref is any
        print("Please try again, none of our tables are ready!")
        return 2


# checkout(): Removes customer from the table, freeing up space for next customer
def checkout(table):
    global tables, alerts

    # print(tables[table])
    alerts.append("\n>>> {0} has paid their bill of {1:.2f}, and table {2} in the {3} has been cleared."
                  .format(tables[table]["customer"].title(), random.uniform(50, 150), table
                          , tables[table]["location"].title()))
    tables[table]["seated"] = 0
    tables[table]["customer"] = ""
    print(threading.current_thread().getName(), 'Exiting')

# seatCustomer(): Assigns a customer to a table, and changes the table's availability for future customers
def seatCustomer(table, customer, partySize):
    global tables, threads

    tables[table]["customer"] = customer
    tables[table]["seated"] = partySize
    # print(tables[table])
    print("Wonderful. We've placed you at table {}, {}. Enjoy your meal.\n\n".format(table, customer.title()))

    t = threading.Timer(random.randint(3, 10), checkout, [table])
    threads.append(t)
    t.start()


if __name__ == '__main__':
    # First, let's establish a dictionary of tables and presumed placements within the restaurant.
    # ready: seats that are ready for a customer (assume ready is fixed)
    # seated: seats currently occupied by a customer (cannot exceed ready)
    tables = {
        "1a": {"ready": 2, "seated": 0, "location": "bar", "customer": ""},
        "1b": {"ready": 2, "seated": 0, "location": "bar", "customer": ""},
        "1c": {"ready": 2, "seated": 0, "location": "bar", "customer": ""},
        "2a": {"ready": 5, "seated": 0, "location": "lounge", "customer": ""},
        "2b": {"ready": 4, "seated": 0, "location": "lounge", "customer": ""},
        "2c": {"ready": 6, "seated": 0, "location": "lounge", "customer": ""},
        "3a": {"ready": 10, "seated": 0, "location": "mezzanine", "customer": ""},
        "3b": {"ready": 12, "seated": 0, "location": "mezzanine", "customer": ""}
    }
    areas = {
        'bar': 2,
        'lounge': 6,
        'mezzanine': 12
    }
    alerts = []
    threads  = []

    print('\n\n\n\n\n')

    while True:
        name = str(input("Good evening, what is your name: "))
        print("Thank you, " + name.title() + ".")
        partySize = takePartySize()
        # Loop to take user input for place. Will continue until party size matches location preference conditions.
        while True:
            preference = str(input("\nWhere would you like to be seated tonight? You can type 'help' to see our options, "
                                   "or enter 'any' if you do not have a preference: ")).lower()
            if preference == 'help':
                printAllRooms()
            else:
                if isValidArea(preference):
                    print("Sorry, your preferred location is unavailable. Please try again.")
                else:  # valid area
                    result = checkSeats(partySize, name, preference)
                    if result != 2:
                        break

        seatCustomer(result, name, partySize)