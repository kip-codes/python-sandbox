# File: unchanged_magicians
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 11/09/2017 at 8:16 PM
#
# For inquiries about the file please contact the author.


def showMagicians(magicians):
    if type(magicians) is list:
        for x in magicians:
            print(x.title())


def makeGreat(magicians):
    greatMagis = []
    if type(magicians) is list:
        for x in magicians:
            greatMagis.append(x + " the Great")
    return greatMagis


if __name__ == '__main__':
    print('* ' * 20)
    tiy8_9 = '8-9. Magicians:\nMake a list of magician names. Pass the list to a function called showMagicians(),' \
             ' which prints the name of each magician in the list.'

    magicians = ['mark', 'lucifer', 'thomas']
    print('showMagicians() will simply traverse the list.')
    showMagicians(magicians)

    print('\nmakeGreat() will take a copy of the list and return a new list.')
    greatMagis = makeGreat(magicians[:])
    print('Great magis are here:')
    showMagicians(greatMagis)
    print('...while the original list remains unedited.')
    showMagicians(magicians)

