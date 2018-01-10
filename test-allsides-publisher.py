# References
#
# Basic HTTP requests
# https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html
# ----------------------------------------------------------------------------------------------------------------------
import requests

from AllSidesItem import *

r = requests.get('https://www.allsides.com/blank/slider/simple/center.json')

articles_as_json = r.json()
allsidesItems = []

for item_as_json in articles_as_json['Items']:
    allsidesItems.append(AllSidesItem(item_as_json))

for allsidesItem in allsidesItems:
    print(allsidesItem)
    break
