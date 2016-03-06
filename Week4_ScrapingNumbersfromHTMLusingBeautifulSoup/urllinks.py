# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter: ')
Incnt = int(raw_input('Enter Count: '))
Inpos = int(raw_input('Enter position: '))-1
html = urllib.urlopen(url).read()
#html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Josan.html').read()
#soup = BeautifulSoup(html)


for i in range(Incnt, 0,-1):
    print 'i', i
    soup = BeautifulSoup(html)
    pos = 0
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print 'Retrieving ',pos,':',tag.get('href', None)
        if( pos == Inpos): 
            html = urllib.urlopen(tag.get('href', None)).read()
            break
        pos +=1

print tag.get('href', None)


    
