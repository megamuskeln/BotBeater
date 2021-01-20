import os
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def startBrowser(site):
    driver = webdriver.Firefox()
    driver.get(site)

    print(driver.find_element_by_class_name('sectionButton'))

def getSites(path):
    with open(path) as file:
        sitesFile = json.load(file)

    sitesFile = sitesFile["sites"]
    sites = {}
    for site in sitesFile:
        url = site["siteURL"] + site["ps5Path"]
        sites[site["siteName"]] = url
    return sites


def startBot():
    sitesPath = os.path.abspath("..//config//sites.json")
    sites = getSites(sitesPath)
    startBrowser(sites["GAME"])


if __name__ == "__main__":
    startBot()
