import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}"
city = "los angeles"
start = 0

url = base_url.format(city)
url += '&start=' + str(start)

with open('yelp_20_pages.txt', 'w') as file:
	count = 0
