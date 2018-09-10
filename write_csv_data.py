import requests
import csv
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}&start={}"
city = "los+angeles"
start = 0
file_path = f'yelp-{city}-clean.csv'

def get_length(file_path):
	with open(file_path) as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
	return len(reader_list)


while start < 60:
		print(start)
		url = base_url.format(city, start)
		response = requests.get(url)
		print(f"STATUS CODE: {response.status_code} FOR {response.url}")
		soup = BeautifulSoup(response.text, 'html.parser')
		businesses = soup.findAll('div', {'class': 'biz-listing-large'})

		with open(file_path, 'a', newline='') as csvfile:
			fieldnames = ['id', 'title', 'address', 'phone']
			reader = csv.DictReader(csvfile, fieldnames=fieldnames)
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			count = 0
			if start == 0:
				writer.writeheader()
			for biz in businesses:
				first_line = ""
				second_line = ""
				phone_number = ""

				title = biz.find('a', {'class': 'biz-name'}).text
				# print(address)
				count += 1
				
				try:
					address = biz.find('address').contents
					for item in address:
						if "br" in item:
							first_line += item.getText() + " "
						else:
							second_line += item.strip(" \n\r\t") + " "
				except Exception as e:
					print(e)
					address = None
					logs = open('errors.log', 'a')
					logs.write(str(__file__) + '-- STARTS' + '\n')
					logs.write(str(e) + '\n')
					logs.write(str(__file__) + '-- ENDS' + '\n\n')
					logs.close()

				try:
					region = biz.find('span', {'class': 'neighborhood-str-list'}).contents
					for item in region:
						if "br" in item:
							first_line += item.getText() + " "
						else:
							second_line += item.strip(" \n\t\r") + " "
				except Exception as e:
					print(e)
					first_line = None
					second_line = None
					logs = open('errors.log', 'a')
					logs.write(str(__file__) + '-- STARTS' + '\n')
					logs.write(str(e) + '\n')
					logs.write(str(__file__) + '-- ENDS' + '\n\n')
					logs.close()

				try:
					phone = biz.find('span', {'class': 'biz-phone'}).contents
					for item in phone:
						if "br" in item:
							phone_number += item.getText() + " "
						else:
							phone_number += item.strip(" \n\t\r") + " "
				except Exception as e:
					print(e)
					phone_number = None
					logs = open('errors.log', 'a')
					logs.write(str(__file__) + '-- STARTS' + '\n')
					logs.write(str(e) + '\n')
					logs.write(str(__file__) + '-- ENDS' + '\n\n')
					logs.close()

				detail = f"{title}\n{second_line}\n{phone_number}\n"
				print(detail)

				next_id = get_length(file_path)

				try:
					writer.writerow({
						'id': next_id,
						'title': title,
						'address': second_line,
						'phone': phone_number
					})
				except Exception as e:
					logs = open('errors.log', 'a')
					logs.write(str(__file__) + '-- STARTS' + '\n')
					logs.write(str(e) + '\n')
					logs.write(str(__file__) + '-- ENDS' + '\n\n')
					logs.close()

		start += 30
