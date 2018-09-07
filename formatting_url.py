import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}"
city = "los angeles"
start = 120

url = base_url.format(city)

third_page = url + '&start=' + str(start)

response = requests.get(third_page)

print(f"STATUS CODE: {response.status_code} FOR {response.url}")

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.findAll('a')
