# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#read the starting point which is  http://py4e-data.dr-chuck.net/known_by_Fikret.html or http://py4e-data.dr-chuck.net/known_by_Torrie.html for the assignment
url = input('Enter - ')



# Retrieve all of the anchor tags

position=18 #passing 17 as index so not really necessary
repeat=1
numberofrepeats=7
while repeat <= numberofrepeats:
    link=[]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url=tags[position-1].get('href',None)
    print(url)
    repeat+=1




    #html = urllib.request.urlopen(url, context=ctx).read()
    #soup = BeautifulSoup(html, 'html.parser')

