import requests
import json
import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

def parseArgos(site):
    ps5Page = requests.get(site)
    soup = bs(ps5Page.content, 'html.parser')
    console = soup.find("h1", { "id" : "h1title" })
    print(console)
    for child in console:
        if (child == "Sorry, PlayStation®5 is currently unavailable."):
            print("Still out of stock")
            return False
        return True



def parseGAME(site):
    start = time.time()
    headers = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "accept": "*/*",
    "referer": "https://www.game.co.uk/",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    }
    ps5Page = requests.get("https://assets.game.net/_master/hardwarePages/playstation5/merch/LaunchCopyAvail/ps5.js?_=1610833181756", headers=headers).text

    discEd = {}

    begin = ps5Page.find('contentPanelsThree')
    end = ps5Page[begin:].find(']')
    beginj = ps5Page[begin:begin + end].find('{')
    beginJson = begin + beginj
    firstbracket = ps5Page[beginJson:begin + end].find('}') + 1
    secondbracket = ps5Page[beginJson + firstbracket:begin + end].find('}') + 1
    closeJson = beginJson + firstbracket + secondbracket
    discEd = json.loads(ps5Page[beginJson:closeJson].replace("'", '"'))
    end = time.time()
    print("Time taken: ", end - start)
    return checkGAMEStock(discEd)
    # soup = bs(ps5Page.content, 'html.parser')
    # for div in soup.findAll('div', attrs={'class' : 'bs-container'}):
    #     print(div.text)#



def checkGAMEStock(ed):
    if ed['button']['copy'] == "Out of stock":
        print("GAME: Out of Stock")
        return False
    return True
