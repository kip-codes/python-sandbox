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
print tiy7_2

print("\nTo make things more interesting I will make restaurant capacity static, but available seats dynamic. "
      "\nThat is, tables will become available after some time.")

# BEGIN SOLUTION
import time, threading

def hello():
    print("hello, Timer")

#checkSeats(): Check how many seats at a table are ready for a customer.
def checkSeats(toSeat, partyName, locPref):
    global tables #this allows access to the tables variable defined in main
    for table in tables:
        if table["location"] == locPref:
            if all(set(table["seated"] > 0)): #check if their preferred seating area is available
                print("I'm sorry " + partyName + ", but our tables in the " + locPref + " are currently occupied.")
                return 2


if __name__ == '__main__':
    # t = threading.Timer(3.0, hello)
    # t.start()

    #First, let's establish a dictionary of tables and presumed placements within the restaurant.
    #ready: seats that are ready for a customer (assume ready is fixed)
    #seated: seats currently occupied by a customer (cannot exceed ready)
    tables = {
        "1a" : {"ready":2, "seated":0, "location":"bar"},
        "1b" : {"ready":2, "seated":0, "location":"bar"},
        "1c" : {"ready":2, "seated":0, "location":"bar"},
        "2a" : {"ready":5, "seated":0, "location":"lounge"},
        "2b" : {"ready":4, "seated":0, "location":"lounge"},
        "2c" : {"ready":6, "seated":0, "location":"lounge"},
        "3a" : {"ready":10, "seated":0, "location":"mezzanine"},
        "3b" : {"ready":12, "seated":0, "location":"mezzanine"}
    }

