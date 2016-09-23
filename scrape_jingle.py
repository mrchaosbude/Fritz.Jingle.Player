import urllib
import urllib.request
from  bs4 import BeautifulSoup

theLink =[]
thetext =[]

def scrapy():
    theurl ="http://www.fritz.de/sehen-und-hoeren/jingles/index.html"
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")
    for link in soup.find_all("a", {"class": "ico ico_download"}):
        theLink.append (link['href'])

    for name in soup.find_all("span", {"class": "manualteasertitle"}):
        thetext.append (name.text)
    thetext.pop(0) #der erste eintrag wird entfernt da er nicht benötigt wird
    nu = 26
    print(thetext[nu])
    print(theLink[nu])

scrapy()