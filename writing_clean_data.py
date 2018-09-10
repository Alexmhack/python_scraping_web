import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}&start={}"
city = "los+angeles"
start = 0
file_path = f'yelp-{city}-clean.txt'

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
			first_line = ""
			second_line = ""
			phone_number = ""
			try:
				title = biz.find('a', {'class': 'biz-name'}).text
				address = biz.find('address').contents
				# print(address)
				phone = biz.find('span', {'class': 'biz-phone'}).contents
				region = biz.find('span', {'class': 'neighborhood-str-list'}).contents
				count += 1
				for item in address:
					if "br" in item:
						first_line += item.getText() + " "
					else:
						second_line += item.strip(" \n\r\t") + " "
				for item in region:
					if "br" in item:
						first_line += item.getText() + " "
					else:
						second_line += item.strip(" \n\t\r") + " "
				for item in phone:
					if "br" in item:
						phone_number += item.getText() + " "
					else:
						phone_number += item.strip(" \n\t\r") + " "

			except Exception as e:
				print(e)
				logs = open('errors.log', 'a')
				logs.write(str(e) + '\n')
				logs.close()
				address = None
				phone_number = None
				region = None

			detail = f"{title}\n{second_line}\n{phone_number}\n"
			print(detail)

			try:
				textFile.write(str(detail) + '\n\n')
			except Exception as e:
				logs = open('errors.log', 'a')
				logs.write(str(e) + '\n')
				logs.close()

	start += 30
