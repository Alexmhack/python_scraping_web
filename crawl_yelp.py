import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}"
city = "los angeles"

url = base_url.format(city)

with open('yelp_20_pages.txt', 'w') as file:
	count = 0
	all_links = []
	start = 0

	for i in range(100):
		url += '&start=' + str(start)
		response = requests.get(url)
		start += 30
		if start == 540:
			break
		print(f"STATUS CODE: {response.status_code} FOR {response.url}")
		soup = BeautifulSoup(response.text, 'html.parser')
		links = soup.findAll('a')
		for link in links:
			if response.status_code == 200:
				href = link.get('href', '')
				if 'https:' in href:
					if href not in all_links:
						all_links.append(href)
						print(href)
						file.write(href + '\n\n')
						count += 1
					else:
						print('ALREADY EXISTS...')
			else:
				print('404 -- SKIPPING')
	print(f"{count} REQUESTED...")
