# File: sandwiches
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 11/11/2017 at 3:26 PM
#
# For inquiries about the file please contact the author.
import sys

def makeSandwich(*items):
    print(items)
    if len(items) == 0:
        print('Your sandwich has no ingredients in it!\n')
        return
    elif len(items) == 1:
        print('Your sandwich has one ingredient:')
    else:  #items >= 2
        print('Your sandwich has {} ingredients:'.format(len(items)))

    for num, item in enumerate(items,1):
        print('{0}.   {1}'.format(num, item))

    print('\n')


if __name__ == '__main__':
    print('* '*20)
    tiy8_12 = '8-12. Sandwiches:\nWrite a function that accepts a list of items a person wants on a sandwich.\nThe ' \
              'function should have one parameter that collects as many items as the function call provides, and it ' \
              'should print a summary of the sandwich that is being ordered.'
    print(tiy8_12)

    ingredients = []
    moreIngredients = ['pickle ricks']
    manyIngredients = ['pickle ricks','salami','mayonnaise']

    makeSandwich(ingredients)  #for some reason this list is considered without any traversal
    makeSandwich()  #a call without any parameters returns the correct value
    makeSandwich(moreIngredients)  #same as before, a list of 1 item is considered as a whole, unintended
    makeSandwich('pickle ricks','salami','mayonnaise')
    makeSandwich(manyIngredients, 'lettuce')

    makeSandwich('cheese')

    makeSandwich('')
