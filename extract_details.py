import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}"
city = "los angeles"
start = 30

url = base_url.format(city)

third_page = url + '&start=' + str(start)

response = requests.get(third_page)

print(f"STATUS CODE: {response.status_code} FOR {response.url}")

soup = BeautifulSoup(response.text, 'html.parser')

businesses = soup.findAll('div', {'class': 'biz-listing-large'})

count = 0
for biz in businesses:
	title = biz.find('a', {'class': 'biz-name'}).text
	print(title)
	address = biz.find('address').text
	print(address)
	phone = biz.find('span', {'class': 'biz-phone'}).text
	print(phone)
