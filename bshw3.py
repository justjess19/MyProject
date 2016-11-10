#bshw3.py

import requests
from bs4 import BeautifulSoup
import re

base_url = "http://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")

words = soup.find_all('p')
for elt in words:
	element = elt.text
	paragraph = re.findall('\\bstudent\\b', element)
	print (paragraph)
	element = re.sub('\\bstudent\\b', "AMAZING student", element)
	print (element)

link = soup.find_all('img')

for a in link:
	href = a['src']
	if (href) == 'https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg':
		a['src'] = "http://gupshupcorner.net/wp-content/uploads/2015/01/Cute-Baby-HD-Wallpaper13.jpg"

for a in link:
	href = a['src']
	if not href.startswith("http:"):
		print("before changing", a['src'])
		a['src'] =  'https://raw.githubusercontent.com/cvanlent/SI206/master/HW3-StudentCopy/media/logo.png'

result = str(soup)

f = open('project.html', "w")
f.write(result)
f.close()