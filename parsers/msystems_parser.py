import requests
from bs4 import BeautifulSoup
import re
from time import sleep
from playsound import playsound

def msystems(toSearch, targetPrice):

	response = requests.get("https://www.msystems.gr/database/select_search_products.php?keywords={0}+&page_num=1&limit=100&orderby=price_asc".format(toSearch))
	soup = BeautifulSoup(response.text, 'html.parser')

	items = soup.find_all("div", class_="list-group-item")
	itemsFound = []

	for item in items:
		if item.findChild("span", class_="category-availability-success"):
			codeInTitle = re.findall("\[.*\]", item.a["title"])
			price = float(re.findall("[\d\.,]+",item.findChild("span", class_="cat-prod-price").text)[0].replace(".","").replace(",","."))

			if len(codeInTitle) > 0:
				titleWithoutCode = item.a["title"].replace(codeInTitle[0], "")
				
				if "RTX" in titleWithoutCode and price <= targetPrice:
					itemsFound.append(item.a.get("href"))

			else:
				if "RTX" in item.a["title"] and price <= targetPrice:
					itemsFound.append(item.a.get("href"))

	results = []

	with open("blacklists/msystems_blacklist.txt", "a+") as f:
		flines = f.readlines()

		for item in itemsFound:
			if item not in [fline.strip() for fline in flines]:
				results.append("https://www.msystems.gr{0}".format(item))
				#playsound("alarm.mp3")
				#f.write("{0}\n".format(item))

			else:
				pass

	sleep(5)
	return results
