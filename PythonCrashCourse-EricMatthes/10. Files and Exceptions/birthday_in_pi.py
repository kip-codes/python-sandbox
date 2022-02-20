# File: birthday_in_pi
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 12/02/2017 at 6:46 PM
#
# For inquiries about the file please contact the author.

from datetime import datetime


def welcomeMessage():
    print('Welcome! This program will allow you to see if your birthday is in the first million digits of pi.')


def takeFullBirthday():
    global birthday
    correctBirthday = False
    while not correctBirthday:
        birthday = input('Please enter the month, day, and year of your birthday in the format (mm/dd/yyyy), '
                         'or \'q\' to quit: ')
        if birthday == 'q':
            return None
        date_object = datetime.strptime(birthday, '%m/%d/%Y')
        print(date_object.strftime('%B %d, %Y'))
        confirm = input('Is this your birthday? (y/n): ').lower()
        if confirm == 'yes' or confirm == 'y':
            correctBirthday = True
        elif confirm == 'no' or confirm == 'n':
            print('That\'s ok. Let\'s start over.\n')
        return birthday.replace('/', '')


def convertSimpleBirthday(birthday):
    birthday = birthday[:4] + birthday[6:]
    return (birthday)


def readPi(filename):
    with open(filename) as file:
        lines = file.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
    return pi_string


if __name__ == '__main__':
    filename = '/Users/kevinip/Documents/GitHub/PythonCrashCourse-EricMatthes/Resources/ehmatthes-pcc_2e-078318e' \
               '/chapter_10 '
    pi_million_digits = readPi(filename)

    welcomeMessage()
    bd = takeFullBirthday()
    simple_bd = convertSimpleBirthday(bd)
    if bd:
        if bd in pi_million_digits:
            print('\nYour full birthday appears in the first million digits of pi!')
            if simple_bd in pi_million_digits:
                print('And its simplified format (mmddyy) is also in the first million digits! Wow!')
            else:
                print('However, the simplified format (mmddyy) is not in the first million digits.')
        else:
            print('\nYour full birthday does not appear in the first million digits of pi.')
            if simple_bd in pi_million_digits:
                print('However, the simplified format (mmddyy) is there! Congratulations!')
            else:
                print('The simplified format (mmddyy) is also absent from the first million digits. Sorry!')
