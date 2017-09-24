# File: personal_message
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 09/23/2017 at 5:33 PM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print("2-3. Personal Message: Store a person's name in a variable, and print a message to that person.\n"
      "Your message should be simple, such as, \"Hello Eric, Would you like to learn some Python today?\" (p. 29)\n")

# Begin solution
person = "Vanessa Williams"
# print(person.partition(' ')[0]) # splits by whitespace and selects the first word


message = "Hello " + person.partition(' ')[0] + ", would you like to learn some Python today?"
print(message)
# End solution