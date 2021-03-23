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


def notify(results):
	if len(results) > 0:
		for result in results:
			print("{0} - Found one! > {1}".format(now.strftime("%d-%m-%Y %H:%M:%S"), result))
			#webhook = DiscordWebhook(url=webhookUrl, content="@everyone found one! > {0}".format(result))
			#response = webhook.execute()


for item in list(itemsDict.keys()):
	now = datetime.datetime.now()
	print("{0} - Searching for {1} price {2}".format(now.strftime("%d-%m-%Y %H:%M:%S"), item, itemsDict[item]))
	
	notify(msystems(item, itemsDict[item]))
	notify(visionstudio(item, itemsDict[item]))
	notify(skroutz(item, itemsDict[item]))
