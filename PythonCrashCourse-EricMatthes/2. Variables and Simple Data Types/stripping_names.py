# File: stripping_names
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 09/23/2017 at 6:16 PM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print("2-7. Store a person's name, and include whitespace characters at the beginning and end of the name."
      "Make sure you use each character combination, \"\\t\" and \"\\n\", at least once. (p. 29)")

# Begin solution
name = " \tVanessa Williams  \n"

print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
# End solution