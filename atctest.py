import urllib2
from BeautifulSoup import BeautifulSoup
import re

# Get top 50 streams
p = re.compile(ur'\/search\/\?icao=([a-zA-Z]*)')
top50url = "http://www.liveatc.net/topfeeds.php"

response = urllib2.urlopen(top50url)
html = response.read()
soup = BeautifulSoup(html)
streamList = str(soup.findAll('table')[7])
top50icao = re.findall(p, streamList)
