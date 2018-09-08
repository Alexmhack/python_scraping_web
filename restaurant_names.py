import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}&start={}"
city = "los angeles"
file_path = 'los_angeles_restaurants.txt'

def extract_names(city, file_path):
	with open(file_path, 'a') as file:
		start = 0
		for i in range(100):
			url = base_url.format(city, start)
			response = requests.get(url)
			start += 30
			print(f"STATUS CODE: {response.status_code} FOR {response.url}")
			soup = BeautifulSoup(response.text, 'html.parser')
			names = soup.findAll('a', {'class': 'biz-name'})

			count = 0
			for info in names:
				try:
					title = info.text
					print(title)
					file.write(title + '\n')
					count += 1
				except Exception as e:
					print(e)
			print(f"{count} RESTAURANTS EXTRACTED...")
			print(start)
			if start == 990:
				break


extract_names(city, file_path)
