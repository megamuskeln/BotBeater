import sys
import time
import json
import requests
import threading
from bot_modules import threads, checkStock


def startSite(sitesPath, cardsPath):
    with open(sitesPath) as file:
        sitesFile = json.load(file)

    sitesFile = sitesFile["sites"]
    sites = {}
    for site in sitesFile:
        url = site["siteURL"] + site["ps5Path"]
        sites[site["siteName"]] = url

    print(sites)
    runSiteThread(sites)

def runSiteThread(sites):
    if checkStock.parseGAME(sites["GAME"]):
