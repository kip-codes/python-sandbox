# File: city_names
# Project: python-sandbox
# Local author: kevin
# Created on 10/29/2017 at 6:31 PM
#
# For inquiries about the file please contact the author.

# cityCountry(): returns string formatted as, "<city>, <country>"
def cityCountry(city='', country=''):
    if not city and country:  # only country is given value
        return "Welcome to {} -- feel free to explore any city!".format(country)
    elif not country and city:  # only city is given value
        return "Welcome to {} -- a city of many in this country.".format(city)
    elif not country and not city:  # Neither city nor country are given values
        return "You seem lost. Do you need directions?"
    else:  # Both country and city are given values
        return "Welcome to {0}, {1}!".format(city, country)


if __name__ == '__main__':
    print('* ' * 20)
    tiy8_6 = "8-6. City Names:\nWrite a function called cityCountry() that takes in the name of a city and its country" \
             "\nCall your function with at least three city-country pairs, and print the value that's returned.\n"
    print(tiy8_6)

    print("With no parameters: ", cityCountry())
    print("With a single parameter, albeit incorrect: ", cityCountry('USA'))
    print("With only a specific parameter (country): ", cityCountry(country='USA'))
    print("With only a specific parameter (city): ", cityCountry(city='Los Angeles'))
    print("With specific ordering of parameter input: (country=<>, city=<>)", cityCountry(country='China', city='Kowloon'))
    print("Standard function call: ", cityCountry('San Jose', 'USA'))

