# File: cars
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 11/11/2017 at 4:13 PM
#
# For inquiries about the file please contact the author.


def makeCar(manufacturer, model, **kwarg):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in kwarg.items():
        car[key] = value

    return car

if __name__ == '__main__':
    mycar = makeCar('honda', 'civic')
    print(mycar)

    mycar = makeCar('honda', 'civic', miles=250000, color='grey-blue', cassette='no')
    print(mycar)