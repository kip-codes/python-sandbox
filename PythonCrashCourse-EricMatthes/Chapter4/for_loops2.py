# File: for_loops2
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 09/24/2017 at 1:21 AM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* ' * 20)
print("The following are small tasks for TiY's 4-3 to 4-9.")

for n in range(1,21):
    print n

mil = []
for n in range(1, 1000000+1):
    mil.append(n)

print min(mil), max(mil)
print sum(mil)

twenty = [x for x in range(1,21,2)]
print twenty

mult_three = [x for x in range(3,30,3)]
print mult_three

cubes = [x**3 for x in range(1,10+1)]
print cubes
