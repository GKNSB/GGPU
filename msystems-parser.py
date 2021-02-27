import requests
from bs4 import BeautifulSoup
import re
from time import sleep
from playsound import playsound

while(True):

	response = requests.get("https://www.msystems.gr/database/select_search_products.php?keywords=3060+&page_num=1&limit=100&orderby=price_asc")
	soup = BeautifulSoup(response.text, 'html.parser')

	items = soup.find_all("div", class_="list-group-item")
	itemsFound = []

	for item in items:
		if item.findChild("span", class_="category-availability-success"):

			codeInTitle = re.findall("\[.*\]", item.a["title"])

			if len(codeInTitle) > 0:
				titleWithoutCode = item.a["title"].replace(codeInTitle[0], "")
				if "RTX" in titleWithoutCode:
					itemsFound.append(item.a.get("href"))

			else:
				if "RTX" in item.a["title"]:
					itemsFound.append(item.a.get("href"))

	for item in itemsFound:
		print("https://www.msystems.gr{0}".format(item))
		playsound("alarm.mp3")

	sleep(10)
