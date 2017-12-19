# File: api
# Project: python-sandbox
# Local author: kevin
# Created on 12/19/2017 at 12:37 AM
#
# For inquiries about the file please contact the author.

# This program is a basic introduction to API integration and my attempt to understand ETL:
# Extract: Retrieve the data from API callbacks or from local databases.
# Transform: Manipulate the data in a way that is useful to ad hoc analysis.
#

import urllib.request
import json
import csv


def locu_search(query_city, query_category):
    """Parses JSON for the name of the restaurant and its phone number and exports to CSV."""

    # This API key is taken from the tutorial I followed and belongs to Justin Mitchel.
    locu_api = '9fb8cd70cb34cab8e83690473133f51943b5c93f'
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + locu_api
    locality = query_city.replace(' ', '%20')  # replaces with a space formatted for a URL
    category = query_category.replace(' ', '%20')
    final_url = url + '&locality=' + locality + '&category=' + category

    # url = 'https://api.locu.com/v1_0/venue/search/?locality=Newport%20Beach&category=restaurant&api_key=' + locu_api
    json_obj = urllib.request.urlopen(final_url)
    data = json.load(json_obj)

    #print(data['objects'])
    # print(data['objects'][0]['name'])
    # print(data['objects'][0]['phone'])

    csv_name = query_city.replace(' ','') + '_' + query_category.replace(' ','') + '.csv'

    with open(csv_name, 'w') as csv_file:
        # writer = csv.writer(csv_file, delimiter=',')  # not needed because already in CSV format

        # Writing headers (titles)
        columnTitleRow = ''
        for key in list(data['objects'][0]):
            columnTitleRow += key + ','
        csv_file.write(columnTitleRow + '\n')

        # Writing row data: extract all data pulled for a restaurant
        for item in data['objects']:  # JSON object of a specific restaurant
            row = ''  # start with an empty row for each restaurant
            for key, value in item.items():
                if type(value) is str:
                    row += value + ','
                elif type(value) is list:
                    for element in value:
                        row += element + ','
            csv_file.write(row + '\n')
    csv_file.close()


if __name__ == '__main__':
    query_city = input("Please enter the city you would like to search for local restaurants: ")
    query_category = input("Please enter the type of business you are looking for: ")
    locu_search(query_city, query_category)