#!/usr/bin/env python3

'''
Never suffer from having to choose which episode of
Star Trek: The Next Generation to watch again...

Trey Fortmuller
'''

import random
import os
import xml.etree.ElementTree as et

def readXML():
	base_path = os.path.dirname(os.path.realpath(__file__))
	xml_file = os.path.join(base_path, "episodes.xml")
	tree = et.parse(xml_file)
	root = tree.getroot()

	all_episodes = []
	for season in root:
		title_list = []	

		for episode in season:
			title = episode[0]
			title_list.append(title.text)
		
		all_episodes.append(title_list)

	return all_episodes

def outputChosen(season, ep):
	chosen = titles_in_season[ep]

	print("TNG CHOOSER HAS CHOSEN:\n")
	print("\tSeason " + str(season+1) + ", Episode " + str(ep+1) + ": " + chosen) 


all_episodes = readXML()
print("TNG EPISODE CHOOSER\n")

usecase = input("Enter 1 to return an episode from the whole series.\nEnter 2 to select a season first...\n")

if usecase == 1:
	# randomly select a season, randomly select an episode, print it
	rand_season = random.randint(0, 7) # random number between 0 and 6 inclusive
	titles_in_season = all_episodes[rand_season]
	rand_ep = random.randint(0, len(titles_in_season))

	outputChosen(rand_season, rand_ep)
elif usecase == 2:
	user_select = input("Which season do you want to see?\n")
	select_season = user_select-1 # to 0 index the choice
	# randomly select an episode from the selected season, print it
	titles_in_season = all_episodes[select_season]
	rand_ep = random.randint(0, len(titles_in_season))

	outputChosen(select_season, rand_ep)
else:
	print("That's not an option.")
	
