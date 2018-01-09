# References
#
# Basic HTTP requests
# https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html
# ----------------------------------------------------------------------------------------------------------------------
import requests
r = requests.get('https://www.allsides.com/blank/slider/simple/center.json')
print(r.json())