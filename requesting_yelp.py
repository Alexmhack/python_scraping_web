import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&ns=1"
response = requests.get(url)

print(response)
print(f"STATUS CODE: {response.status_code}")
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
