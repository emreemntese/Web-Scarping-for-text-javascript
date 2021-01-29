import requests
from bs4 import BeautifulSoup

# scraping site
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

#we have 250 movies (data). we will extract relevant data from each movie's own page.

allhtml = requests.get(url).content
allhtml = BeautifulSoup(allhtml,"html.parser")

# get the each data's url
def geturl(allmovies):
    pass

print(allhtml)
#coming soon
