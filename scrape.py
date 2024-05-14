#from bs4 import BeautifulSoup
import bs4
from urllib.request import urlopen
from urllib.request import Request
#pass the URL
site = "https://www.staples.com/mounts/directory_mounts?pn=1"
hdr = {'User-Agent':'Mozilla/5.0'}
req = Request(site, headers=hdr)
#read the source from the URL
page = urlopen(req)
readHtml = page.read()
#close the url
page.close()
#passing HTML to scrape it
soup = bs4.BeautifulSoup(readHtml, 'html.parser')

tableClassResults = soup.find("div", { "class" : "SearchResults-UX2__searchRow" })
print(tableClassResults)
if tableClassResults:

    mounts = tableClassResults.find_all("div", {"class":"standard-tile__title"})
    cost = tableClassResults.find_all("span", {"class":"standard-tile__ada_hidden"})
#try and make a nested for loop where it cycles through each individual mount then gets 
#name and price. Ensure it loops through all of them
    for prod in mounts:    
        
        #item = prod.find("div", {"class":"standard-tile__title"})
        #if item:
        print("Item:"+prod.text.strip())
        #else:
            #print("item fail")
        #cost = prod.find("div", {"class":"standard-tile__ada_hidden"})
        #if cost:
        
        #else:
        #   print("cost fail")
        #genreClass=titlediv.find(class_="genre")
        #print("Genries:")
        #for eachGenre in genreClass.find_all('a'):
        #    print("\t"+eachGenre.string)
        #print("Run Time:"+titletd.find(class_="runtime").string)
        #rating_rating=titletd.find(class_="rating-rating")
        #ratingValue=rating_rating.find(class_="value")
        #print("Rating:"+ratingValue.string)
    for costs in cost:
        print("Cost:"+costs.text.strip())
else:
    print("Unable to find search results container.")
