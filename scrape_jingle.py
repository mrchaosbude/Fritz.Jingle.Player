import urllib
import urllib.request
from  bs4 import BeautifulSoup

theLink =[]
thetext =[]

def scrapy():
    theurl ="http://www.fritz.de/sehen-und-hoeren/jingles/index.html"
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    for link in soup.find_all("a", {"class": "ico ico_download"}): #sucht die mp3 url
        theLink.append (link['href'])

    for name in soup.find_all("span", {"class": "manualteasertitle"}): #sucht den zur datei gehörigen namen raus
        thetext.append (name.text)
    for x in range(5):
        thetext.pop(0)
    for x in range(4):
        theLink.pop(0)

    return thetext, theLink

if __name__ == "__main__":
    scrapy()