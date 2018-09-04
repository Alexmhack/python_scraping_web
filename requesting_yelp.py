import requests

url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&ns=1"
response = requests.get(url)

print(response)
