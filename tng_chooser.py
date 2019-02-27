#!/usr/bin/env python3

'''
Never suffer from having to choose which episode of
Star Trek: The Next Generation to watch again...

Trey Fortmuller

Usage:
TODO
'''

import random
import os
import xml.etree.ElementTree as et

def readXML():
	base_path = os.path.dirname(os.path.realpath(__file__))
	xml_file = os.path.join(base_path, "episodes.xml")
	tree = et.parse(xml_file)
	root = tree.getroot()

	for season in root:
		for episode in season:
			for title in episode:
				print(title.text, episode.attrib)

# TODO: usage, UI, finish choosing

readXML()

num = random.randint(1, 101) # random int between 1, and 100

print(num)
	
