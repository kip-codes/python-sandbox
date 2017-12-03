# File: learning_files
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 12/02/2017 at 6:07 PM
#
# For inquiries about the file please contact the author.

tiy10_1 = '10-1. Learning Python:\nWrite a program that reads a text file and prints what you wrote three times.\nPrint ' \
          'the contents once by reading in the entire file, once by looping over the file object, and once by storing ' \
          'the lines in a list and then working with them outside the \'with\' block.\n'


def readEntireFile(filename):
    """Read and print contents of entire file."""
    with open(filename) as f:
        print(f.read().rstrip())  # will not print trailing whitespace

def readLoopedFile(filename):
    """Read file by line, then print each line."""
    with open(filename) as f:
        for line in f:
            print(line.rstrip())


def readStoredFile(filename):
    """Read and store contents of a file into a list, then print the contents of the list."""
    pass



if __name__ == '__main__':
    print('* '*20)
    print(tiy10_1)

    filename = '/Users/kevinip/Documents/POST GRAD/PyCharm Projects/PythonCrashCourse/PythonCrashCourse-EricMatthes/10. Files and Exceptions/learning_files.txt'

    readEntireFile(filename)
    print('* ' * 3)
    readLoopedFile(filename)
    print('* ' * 3)