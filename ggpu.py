from parsers.msystems_parser import msystems
from parsers.visionstudio_parser import visionstudio
from parsers.skroutz_parser import skroutz
from discord_webhook import DiscordWebhook
import configparser
import datetime
import json


config = configparser.RawConfigParser()
config.read("configuration.config")
webhookUrl = config.get("Config", "webhookUrl")
items = config.get("Config", "items")
itemsDict = json.loads(items)


def notify(results, searchItem):
	if len(results) > 0:
		for result in results:
			print("{0} - Found a {1}! > {2}".format(now.strftime("%d-%m-%Y %H:%M:%S"), searchItem, result))
			webhook = DiscordWebhook(url=webhookUrl, content="@everyone found a {0}! > {1}".format(searchItem, result))
			response = webhook.execute()


for item in list(itemsDict.keys()):
	now = datetime.datetime.now()
	print("{0} - Searching for {1} price {2}".format(now.strftime("%d-%m-%Y %H:%M:%S"), item, itemsDict[item]))
	
	notify(msystems(item, itemsDict[item]), item)
	notify(visionstudio(item, itemsDict[item]), item)
	notify(skroutz(item, itemsDict[item]), item)
