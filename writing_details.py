import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}&start={}"
city = "los+angeles"
start = 0
file_path = f'yelp-{city}.txt'

while start < 990:
	print(start)
	url = base_url.format(city, start)
	response = requests.get(url)
	print(f"STATUS CODE: {response.status_code} FOR {response.url}")
	soup = BeautifulSoup(response.text, 'html.parser')
	businesses = soup.findAll('div', {'class': 'biz-listing-large'})
	count = 0

	for biz in businesses:
		try:
			title = biz.find('a', {'class': 'biz-name'}).text
			address = biz.find('address').text
			phone = biz.find('span', {'class': 'biz-phone'}).text
			detail = f"{title}\n{address}\n{phone}"
			print(detail)
			count += 1
		except Exception as e:
			print(e)
	start += 30



# with open(file_path, 'w') as textFile:
# 	soup = BeautifulSoup(response.text, 'html.parser')
# 	businesses = soup.findAll('div', {'class': 'biz-listing-large'})
# 	count = 0
# 	for biz in businesses:
# 		title = biz.find('a', {'class': 'biz-name'}).text
# 		address = biz.find('address').text
# 		phone = biz.find('span', {'class': 'biz-phone'}).text
# 		detail = f"{title}\n{address}\n{phone}"
# 		textFile.write(str(detail) + '\n\n')
