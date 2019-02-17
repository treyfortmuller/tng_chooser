import requests
from bs4 import BeautifulSoup

def linePrint(list):
	for elem in list:
		print(elem)

# grab the HTML for the site
website_url = requests.get("https://en.wikipedia.org/wiki/List_of_Star_Trek:_The_Next_Generation_episodes").text

# get tag hierarchy for HTML
soup = BeautifulSoup(website_url,"lxml")
# print(soup.prettify())

# episode tables are in a particular class
episode_tables = soup.findAll("table",{"class":"wikitable plainrowheaders wikiepisodetable"})
# print(episode_tables)

season1 = episode_tables[0]

s1_nuggets = season1.findAll("td",{"class":"summary"})

# linePrint(s1_nuggets)

links = []
for elem in s1_nuggets:
	links.append(elem.find('a'))

# linePrint(links)

s1_titles = []
for link in links:
	s1_titles.append(link.get("title"))

linePrint(s1_titles)