# File: people
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 10/01/2017 at 8:42 PM
#
# For inquiries about the file please contact the author.
import time, sys

# Assignment prompt
print('* ' * 20)
tiy6_7 = "6-7. People\nStart with the program from Exercise 6-1. Make two new dictionaries representing different" \
         " people, and store all three dictionaries in a list called \'people\'." \
         "\nLoop through your list of people, printing everything you know about each person. (p. 114)"
print(tiy6_7)

# BEGIN SOLUTION
# copy of program from 6-1
famous_people = []

person = {
    "first_name" : "Barefoot",
    "last_name" : "Contessa",
    "age" : "timeless",
    "city" : "Chicago"
}
famous_people.append(person)

person = {
    "first_name" : "Michael",
    "last_name" : "Cera",
    "age" : 14,
    "city" : "Probably Milwaukee or something"
}
famous_people.append(person)

# print famous_people

# Let's mix things up and prompt the user to provide input for the last person in our list of dictionaries.
print("\nHello there admin! It seems we have one more spot open for your list of famous people.\n")
# Get first name
first_name = raw_input("What is the first name of this individual?\n")
print("Great, thanks for that.")
# Get last name
last_name = raw_input("And may I have the last name, please?\n")
print("Awesome, this is going swell.")
# Get age
while True:
    try:
        age = float(raw_input("And just how old is this person?\n"))
        if not (0 < age):
            raise ValueError()
    except ValueError:
        print("Oh come on now... let's be nice and give them a real age!\n")
    else:  # success
        print("Wow! And they've accomplished so much!")
        break
# Get city
city = raw_input("Where is this wonderful person from?\n")
print("Well, that city's lucky to have them.")

# terminate input
person = {"first_name" : first_name, "last_name" : last_name, "age" : age, "city" : city}
famous_people.append(person)
print("\nAll set! Returning to main menu...")
time.sleep(2)
# os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal of junk

# Interactive menu
# os.system('clear') <-- will not work in PyCharm IDE, but should work when run in cmd or terminal
print("Welcome to the prototype KEVIN'S FAVORITE FAMOUS PEOPLE app!")
print("= " * 30)

mainmenu_options = ["\n\t1. Create entry in database",
                    "\n\t2. Check status of individuals",
                    "\n\t3. Exit program"]

# Menu options
def addEntry() :
    print("Adding entry...")
    first_name = raw_input("What is the first name of this individual?\n")
    print("Great, thanks for that.")
    # Get last name
    last_name = raw_input("And may I have the last name, please?\n")
    print("Awesome, this is going swell.")
    # Get age
    while True:
        try:
            age = float(raw_input("And just how old is this person?\n"))
            if not (0 < age):
                raise ValueError()
        except ValueError:
            print("Oh come on now... let's be nice and give them a real age!\n")
        else: # success
            print("Wow! And they've accomplished so much!")
            break
    # Get city
    city = raw_input("Where is this wonderful person from?\n")
    print("Well, that city's lucky to have them.")

    # terminate input
    person = {"first_name": first_name, "last_name": last_name, "age": age, "city": city}
    famous_people.append(person)
    print("\nAll set! Returning to main menu...")
    time.sleep(2)

def checkStatus() :
    def editPerson() :
        choice = raw_input("Choose a person by entering their ID, or enter 0 to return to the main menu.\n")
        if int(choice) > len(famous_people):
            print("Your selection was invalid. Please try again.")
            editPerson()
        elif int(choice) > 0 and int(choice) <= len(famous_people): # Choice is valid
            print(famous_people[int(choice)-1]["first_name"].upper() + " " + famous_people[int(choice)-1]["last_name"].upper())

            def deletePerson(choice) :
                del famous_people[int(choice)-1]

            def checkAge(choice) :
                tempAge = famous_people[int(choice)-1]["age"]
                if (tempAge == 1):
                    print("They're just" + str(tempAge) + "year old! How precious!")
                else:
                    print("They're " + str(tempAge) + " years old.")

            def checkCity(choice) :
                tempCity = famous_people[int(choice)-1]["city"]
                print("They're from the wonderful city of " + tempCity + ".\n")

            person_navigation = {
                "1" : deletePerson,
                "2" : checkAge,
                "3" : checkCity
            }

            person_options = ["\n\t1. Delete person from list",
                              "\n\t2. Check this person's age",
                              "\n\t3. Check the city this person came from",
                              "\n\t(Enter 0 to exit to main menu.)"]

            while True:
                for x in person_options:
                    print x,
                action = raw_input("\nWhat would you like to do with this person?\n")
                if int(action) == 0:
                    break
                elif (action in person_navigation):
                    person_navigation[action](choice)  # Execute the choice
                    break
                else:
                    print("Your choice was invalid.")
        else: # catch all errors
            return
    if len(famous_people) == 0:
        while True:
            action = raw_input("Your log of famous people is empty. Would you like to add one now? (y/n)\n")
            if (action.lower() == "y" or action.lower() == "yes"):
                addEntry()
                break
            elif (action.lower() == "n" or action.lower() == "no"):
                break
            else: # Invalid input
                print("Your choice was invalid for this prompt. Please type Yes or No.")
    else:
        print("Accessing the people in your dictionary...")
        for x, i in enumerate(famous_people, 1): # city, first name, last name, age
            print("\t" + str(x)+ ". "),
            print(i["first_name"] + " " + i["last_name"])
        editPerson()

def exitProgram() :
    print("Exiting...")
    time.sleep(1)
    sys.exit()

# function names, to be executed later with ()
mainmenu_navigation = {
    "1" : addEntry,
    "2" : checkStatus,
    "0" : exitProgram
}

# MAIN MENU

while True:
    for x in mainmenu_options:
        print x,
    choice = raw_input('\nWhat would you like to do? (Enter 0 to exit program.)\n')

    if (choice in mainmenu_navigation) :
        mainmenu_navigation[choice]()  # Execute the choice
    else :
        print("Your choice was invalid.")
        sys.exit()


# END SOLUTION