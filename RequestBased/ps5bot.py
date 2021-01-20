import os
import time
import json
import logging
from bot_modules import startSite

def beginBot():
    sitesPath = os.path.abspath("..//config//sites.json")
    cardsPath = os.path.abspath("..//config//card.json")
    # getUserInput()
    startPurchase(sitesPath, cardsPath)
    return



def getUserInput():
    user = " "
    choices = ['Check Stock (1)', 'Start Purchase (2)']
    while True:
        giveUserOptions(choices)
        user = input("$ ")
        if (user == 1):
            return 1
        elif (user == 2):
            return 2



def giveUserOptions(c):
    print("Please select an option from the menu.\n")
    for i in c:
        print(i)

def checkStock():
    ## TODO:
    return

def startPurchase(sitesPath, cardsPath):
    startSite(sitesPath, cardsPath)


if __name__ == "__main__":
    beginBot()
