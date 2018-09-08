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

	with open(file_path, 'a') as textFile:
		count = 0
		for biz in businesses:
			try:
				title = biz.find('a', {'class': 'biz-name'}).text
				address = biz.find('address').text
				phone = biz.find('span', {'class': 'biz-phone'}).text
				count += 1
			except Exception as e:
				print(e)
				logs = open('errors.log', 'a')
				logs.write(str(e) + '\n')
				logs.close()
				address = None
				phone = None

			detail = f"{title}\n{address}\n{phone}"
			print(detail)

			try:
				textFile.write(str(detail) + '\n\n')
			except Exception as e:
				logs = open('errors.log', 'a')
				logs.write(str(e) + '\n')
				logs.close()

	start += 30
