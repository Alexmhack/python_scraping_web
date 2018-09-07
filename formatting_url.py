import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}"
city = "los angeles"

url = base_url.format(city)

response = requests.get(url)

print(f"STATUS CODE: {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.findAll('a')
