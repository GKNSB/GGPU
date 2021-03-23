import requests
from bs4 import BeautifulSoup
import re
from time import sleep
from playsound import playsound

def visionstudio(toSearch, targetPrice):

	checkNextPage = True
	pageToCheck = 1
	itemsFound = []

	while(checkNextPage):

		response = requests.get("https://www.visionstudio.gr/prodlist.asp?cat=5&sub=undefined&pmanuf=undefined&sort=undefined&step={0}&showfoto=0".format(pageToCheck))
		soup = BeautifulSoup(response.text, 'html.parser')

		table = soup.find("table", id="table18")
		trs = table.find_all("tr")

		for tr in trs:
			if str(toSearch) in tr.text and "RTX" in tr.text:

				for img in tr.find_all("img"):
					if "/544.jpg" in img["src"] or "/543.jpg" in img["src"] or "/542.jpg" in img["src"] or "/541.jpg" in img["src"]:

						numbers = re.findall("[\d\.,]+", tr.text)
						price = float(numbers[len(numbers) - 1].replace(",","."))
						if price <= targetPrice:

							itemsFound.append(tr.a.get("href"))

		if len(trs) < 50:
			checkNextPage = False

		pageToCheck = pageToCheck + 1

	results = []

	with open("blacklists/visionstudio_blacklist.txt", "a+") as f:
		flines = f.readlines()

		for item in itemsFound:
			if item not in [fline.strip() for fline in flines]:
				results.append("https://www.visionstudio.gr/{0}".format(item))
				#playsound("alarm.mp3")
				#f.write("{0}\n".format(item))
			
			else:
				pass

	sleep(5)
	return results
