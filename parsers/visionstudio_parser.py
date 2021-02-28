import requests
from bs4 import BeautifulSoup
import re
from time import sleep
from playsound import playsound

def visionstudio():

	checkNextPage = True
	pageToCheck = 1
	itemsFound = []

	while(checkNextPage):

		response = requests.get("https://www.visionstudio.gr/prodlist.asp?cat=5&sub=undefined&pmanuf=undefined&sort=undefined&step={0}&showfoto=0".format(pageToCheck))
		soup = BeautifulSoup(response.text, 'html.parser')

		table = soup.find("table", id="table18")
		trs = table.find_all("tr")

		for tr in trs:
			if "3060" in tr.text and "RTX" in tr.text:
				
				for img in tr.find_all("img"):
					if "/544.jpg" in img["src"] or "/543.jpg" in img["src"] or "/542.jpg" in img["src"] or "/541.jpg" in img["src"]:
						
						itemsFound.append(tr.a.get("href"))

		if len(trs) < 50:
			checkNextPage = False
		pageToCheck = pageToCheck + 1

	for item in itemsFound:
		print("https://www.visionstudio.gr{0}".format(item))
		playsound("alarm.mp3")

	sleep(5)