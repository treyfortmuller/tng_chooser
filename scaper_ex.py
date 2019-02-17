import requests
from bs4 import BeautifulSoup

# grab the HTML for the site
website_url = requests.get("https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area").text

# get tag hierarchy for HTML
soup = BeautifulSoup(website_url,"lxml")
# print(soup.prettify())

# find the wikitable sortable class, where our info resides
my_table = soup.find("table",{"class":"wikitable sortable"})

# the list of countries are within <a> tags
links = my_table.findAll('a')
# for elem in links:
# 	print(elem)

countries = []
for link in links:
	countries.append(link.get("title"))

print(countries)