# # To run this, download the BeautifulSoup zip file
# # http://www.py4e.com/code3/bs4.zip
# # and unzip it in the same directory as this file
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# #read the starting point which is  http://py4e-data.dr-chuck.net/known_by_Fikret.html or http://py4e-data.dr-chuck.net/known_by_Torrie.html for the assignment
# url = input('Enter - ')
#
#
#
# # Retrieve all of the anchor tags
#
# position=18 #passing 17 as index so not really necessary
# repeat=1
# numberofrepeats=7
# while repeat <= numberofrepeats:
#     link=[]
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup('a')
#     url=tags[position-1].get('href',None)
#     print(url)
#     repeat+=1
#
#
#
#
#     #html = urllib.request.urlopen(url, context=ctx).read()
#     #soup = BeautifulSoup(html, 'html.parser')
#------------------------------------------------------------retrieving xml from API -----------

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
# #--------------------------------------------
#
# serviceurl = 'http://py4e-data.dr-chuck.net/comments_1254138.xml'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
#
# url = serviceurl
# print('Retrieving', url)
# uh = urllib.request.urlopen(url, context=ctx)
# data = uh.read()
# print('Retrieved', len(data), 'characters')
# print(data.decode())
# tree = ET.fromstring(data)
# print(tree)
# results = tree.findall('.//count')
# lengthofresults= len(results)
# count=0
# for xml in results:
#     #print (results[i].text)
#     count+=int(xml.text)
#     # #results = tree.findall('result')
#     # #lat = results[0].find('geometry').find('location').find('lat').text
#     # #lng = results[0].find('geometry').find('location').find('lng').text
#     # #location = results[0].find('formatted_address').text
#     #
#     # print('lat', lat, 'lng', lng)
#     # print(location)
# print(count)
#
"""
import json as js
import urllib

# json = '["Number","Pie","tree"]'
# result= js.loads(json)
# print(result)
#
# import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url='http://py4e-data.dr-chuck.net/comments_1254139.json'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
comments=js.loads(data)
print(comments)
print('User count:', len(comments['comments']))
sum=0
lenghtofjsonfile=len(comments)
print(js.dumps(comments['comments'], indent=4, sort_keys=True))#checking the way data is represented
for i in (comments['comments']):
    sum+=i['count']
    #sum += item['count']
print(sum)

"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl


# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))
#---------------
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)


