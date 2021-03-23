import requests
from bs4 import BeautifulSoup
import re
from time import sleep
from playsound import playsound

def skroutz(toSearch, targetPrice):

	checkNextPage = True
	pageToCheck = 1
	itemsFound = []

	while(checkNextPage):

		response = requests.get("https://www.skroutz.gr/c/55/kartes-grafikwn-vga.html?availability_enum=10&page={0}&keyphrase={1}".format(pageToCheck, toSearch), allow_redirects=False)
		soup = BeautifulSoup(response.text, 'html.parser')

		if "You are being" in response.text:
			newUrl = soup.find("a").get("href")
			response = requests.get("{0}&availability_enum=10".format(newUrl), allow_redirects=False)
			soup = BeautifulSoup(response.text, 'html.parser')

		items = soup.find_all("div", class_="card-content")

		for item in items:

			price = float(re.findall("[\d\.,]+", item.find_all("a", class_="js-sku-link sku-link")[0].text)[0].replace(".","").replace(",","."))

			if "RTX" in item.text and price <= targetPrice:
				itemsFound.append(item.a.get("href"))

		if len(items) == 48:
			pageToCheck = pageToCheck + 1

		else:
			checkNextPage = False

	results = []

	with open("blacklists/skroutz_blacklist.txt", "a+") as f:
		flines = f.readlines()

		for item in itemsFound:
			if item not in [fline.strip() for fline in flines]:
				results.append("https://www.skroutz.gr{0}".format(item))
				#print("https://www.skroutz.gr{0}".format(item))
				#playsound("alarm.mp3")
				#f.write("{0}\n".format(item))
			
			else:
				pass

	sleep(5)
	return results
