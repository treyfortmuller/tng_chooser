# web scraper to grab the names of the episodes of each season on TNG
# and saves all the titles to an XML file

import requests
from bs4 import BeautifulSoup
import os
import xml.etree.ElementTree as et

def scrapeWiki():
	# grabs all the seasons from the TNG wiki tables, returns a list of episode tables
	website_url = requests.get("https://en.wikipedia.org/wiki/List_of_Star_Trek:_The_Next_Generation_episodes").text

	# get tag hierarchy for HTML
	soup = BeautifulSoup(website_url,"lxml")

	# episode tables are in a particular class
	episode_tables = soup.findAll("table",{"class":"wikitable plainrowheaders wikiepisodetable"})

	return episode_tables

def getSeason(tables, seasonNumber):
	# return a list of the episodes in a season with cleaned titles
	# pass in the season number (1 indexed) and the episode tables
	season  = tables[seasonNumber - 1]
	title_cells = season.findAll("td",{"class":"summary"})

	links = []
	for elem in title_cells:
		links.append(elem.find('a'))

	season_titles = []
	for link in links:
		season_titles.append(link.get("title"))

	return cleanTitles(season_titles)

def cleanTitles(titles):
	# remove wikipedia clarifiers from the titles of episodes
	cleaned_titles = []
	for title in titles:	
		index = title.find(" (Star Trek: The Next Generation)")

		if (index != -1):
			cleaned = title[:index]
			cleaned_titles.append(cleaned)
		else:
			cleaned_titles.append(title)

	return cleaned_titles

def writeSeasonTxt(season_titles):
	# write the episode names to a text file
	file = open("episodes.txt", "w")
	
	for ep in season_titles:
		file.write(ep + "\n")
	file.close() 

def readTxtFile():
	# example of reading from a text file
	file = open("episodes.txt", "r") 

	ep_from_file = file.readlines()
	print("FROM FILE:")
	print(ep_from_file)

def writeSeasonXML(season_num, season_titles):
	# grab the root of the XML file
	base_path = os.path.dirname(os.path.realpath(__file__))
	xml_file = os.path.join(base_path, "episodes.xml")
	tree = et.parse(xml_file)
	root = tree.getroot()

	# add a new season element to the root
	new_season_num = str(season_num)
	new_season = et.SubElement(root, "season", attrib={"id" : new_season_num})

	for i in range(0, len(season_titles)):
		new_ep = et.SubElement(new_season, "episode", attrib={"id" : str(i+1)})
		new_ep_title = et.SubElement(new_ep, "title")
		new_ep_title.text = season_titles[i]

	tree.write(xml_file)

def linePrint(list):
	# helper function for prettier printing of many lines
	for elem in list:
		print(elem)

### run the script for one season ###
# obtain the tables of episodes from Wikipedia
# episode_tables = scrapeWiki()

# obtain the cleaned titles for season 1
# s1_titles = getSeason(episode_tables, 1) # there are 7 seasons of TNG

# write the season titles to a XML file
# writeSeasonXML(1, s1_titles)

### all the seasons ###
NUM_SEASONS = 7 # there are 7 seasons of TNG

episode_tables = scrapeWiki()

for i in range(0, NUM_SEASONS):
	current_titles = getSeason(episode_tables, i+1) # season labels are 1 indexed

	# write the season to the XML file
	writeSeasonXML(i+1, current_titles)
	


