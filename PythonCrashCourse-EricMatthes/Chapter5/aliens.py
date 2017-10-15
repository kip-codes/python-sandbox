# File: aliens
# Project: python-sandbox
# Local author: kevin
# Created on 09/30/2017 at 1:40 PM
#
# For inquiries about the file please contact the author.

# Assignment prompt
print('* ' * 20)
tiy5_3 = "5-3. Alien Colors #1:\nImagine an alien was just shot down in a game. Create a variable called alien_color" \
         " and assign it a value of \'green\', \'yellow\', or \'red\'. (p. 88)"
tasklist = ["Write an if statement to test whether the alien's color is green. If it is, print a message that the"
            " player just earned 5 points.","Write one version of this program that passes the if test and another that"
            " fails (The version that fails will have no output.)"]
print tiy5_3
for n,task in enumerate(tasklist,1):
    print("Task " + str(n)+ ":\t" + task)

# BEGIN solution
print("\nBEGIN TASK 1...")
alien_color = 'green'
points = 0
losses = 0
print("Is the alien green?")
if alien_color == "green":
    print("Congratulations! You just earned five points.")
    points += 5
else:
    print("The alien is not green. You took some damage.")
    losses += 5


print("\nBEGIN TASK 2...")
print("Scanning for red aboriginals in the distance...")
if (alien_color == "red"):
    print("Artifact spotted! It's red and on the move!!")
    points += 5
else:
    print("There's nothing red in the vicinity... You've taken a loss in resources for the expedition.")
    losses += 3
print("At the end of today's mission, you've earned " + str(points-losses) + " points")

print('\n')
print('* ' * 20)
print("Skipping tiy5-4 to 5-7 due to repetition...")