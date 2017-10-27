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
import time, threading, random, logging, sys

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

    for alert in alerts:
        print(alert)
    del alerts[:]


# takePartySize(): Take input for party size
def takePartySize():
    global areas

    while True:
        try:
            ps = int(input("\nAnd how big is your party: "))
            if ps <= 0:
                raise ValueError()
        except ValueError:
            print("Unacceptable party size. Please try again.")
        else:  # valid integer
            if ps > max(areas.values()):
                print("I'm sorry, your party is too large to be put under one name."
                      " Please try again with a smaller party.")
            else:
                print("Ok, party of " + str(ps) + "...")
                printQueuedMsgs()
                break
    return ps


# checkSeats(): Check how many seats at a table are ready for a customer.
def checkSeats(partySize, name, locPref):
    global tables  # this allows access to the tables variable defined in main
    global waitingList

    # If the customer's preference will not allow for their party size
    if locPref != 'any' and getAreaCap(locPref) < partySize:
        print("I'm sorry, our tables in the {0} cannot seat {1} people. Might I recommend you to some areas that can "
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
                printQueuedMsgs()
                return t

    # If nothing is available for them
    if locPref != 'any':  # prefers a specific seating
        print("I'm sorry " + name.title() + ", but our tables in the " + locPref + " are currently occupied.")
        print("There's currently an estimated waiting period of {} seconds for a table of your size. "
              "We have your name written down already, so we'll call you as soon as one is available! "
              "\nThank you for waiting.\n".format(random.randint(5, 15) * (len(waitingList[locPref])+1)))
        waitingList[locPref].insert(0, [name, partySize])  # adds customer to the queue for the table
        return 1
    else:  # no preference in seating

        # Force assignment of table for waiting list
        new_location = ''
        if partySize <= 2:
            new_location = 'bar'
        elif partySize <= 6:
            new_location = 'lounge'
        else:
            new_location = 'mezzanine'

        print("There's currently an estimated waiting period of {} seconds for a table of your size. "
              "We have your name written down already, so we'll call you as soon as one is available! "
              "\nThank you for waiting.\n".format(random.randint(5, 15) * (len(waitingList[new_location])+1)))
        waitingList[new_location].insert(0, [name, partySize])
        return 1


# checkout(): Removes customer from the table, freeing up space for next customer
def checkout(table):
    global tables, alerts

    # print(tables[table])
    alerts.append(">>> {0} has paid their bill of ${1:.2f}, and table {2} in the {3} has been cleared."
                  .format(tables[table]["customer"].title(), random.uniform(30, 70)*tables[table]['seated']
                          , table.upper(), tables[table]["location"].title()))
    tables[table]["seated"] = 0
    tables[table]["customer"] = ""
    # logging.debug('Exiting')


    # Checks queue for existing customers on the waiting list for this table.
    if waitingList[tables[table]['location']]:
        new_customer = waitingList[tables[table]['location']].pop()  # gets the customer that arrived first
        new_customer_name = new_customer[0]
        new_customer_party = new_customer[1]

        print("\n[!] >>> {}, thank you for waiting -- your table is ready!".format(new_customer_name.title()))
        seatCustomer(table, new_customer_name, new_customer_party)


# seatCustomer(): Assigns a customer to a table, and changes the table's availability for future customers
def seatCustomer(table, customer, partySize):
    global tables, threads

    tables[table]["customer"] = customer
    tables[table]["seated"] = partySize
    # print(tables[table])
    print("Wonderful. We've placed you at table {0}, {1}. Enjoy your meal.\n\n".format(table.upper(), customer.title()))
    printQueuedMsgs()

    t = threading.Timer(random.randint(5, 15), checkout, [table])
    threads.append(t)
    # print(threads)
    t.start()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                        )

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
    threads = []
    waitingList = {
        "bar": [],
        'lounge': [],
        'mezzanine': []
    }

    print('\n\n\n\n\n')

    active = True
    while active:
        name = str(input("Good evening, what is your name (0 to exit): "))
        if name == '0':
            print("Thank you, have a good night!")
            sys.exit()
        print("Thank you, " + name.title() + ".")
        printQueuedMsgs()

        partySize = takePartySize()
        # Loop to take user input for place. Will continue until party size matches location preference conditions.
        while True:
            preference = str(input("\nWhere would you like to be seated tonight? You can type 'help' to see our options, "
                                   "or enter 'any' if you do not have a preference (0 to exit): ")).lower()
            if preference == '0':
                print("Thank you, have a good night!")
                sys.exit()
            if preference == 'help':
                printAllRooms()
            else:
                if isValidArea(preference):
                    print("Sorry, your preferred location is unavailable. Please try again.")
                else:  # valid area
                    result = checkSeats(partySize, name, preference)
                    if result != 2:
                        break
        if result != 1:
            seatCustomer(result, name, partySize)