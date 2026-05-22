from utility import itemToSlug
from apiHandler import getRequest
from colorama import Fore
import keyboard
import time

def getAveragePlat(dictOrders):
    totalPlat = 0

    for order in dictOrders:
        totalPlat += order['platinum']

    averagePlat = totalPlat / 5
    return averagePlat

def queryPlatPrices(listOfItems):
    for item in listOfItems:
        if "Forma" in item:
            print(Fore.RED + "\nForma Blueprint :(" + Fore.RESET)
        elif "Prime" in item:
            print(Fore.YELLOW + item.upper() + Fore.RESET)

            itemSlug = itemToSlug(item)
            #print(f"\n Item slug generated: {itemSlug}. Now querying warframe.market...")
            
            dictOrders = getRequest(itemSlug)

            if type(dictOrders) == list:
                avgPlat = getAveragePlat(dictOrders)
            
                latestPlat = dictOrders[0]['platinum']

                print(Fore.CYAN + f"\t AVERAGE PLATINUM LISTING: " + Fore.RESET +  f"{avgPlat}p")
                print(Fore.CYAN + f"\t LATEST PLATINUM LISTING: " + Fore.RESET +  f"{latestPlat}p")
            else:
                print(f"Something went wrong while querying this item. API returned with status code: {dictOrders}")

    

def scanScreenshot(appState, crop):
    print("Now scanning...")
    listOfItems = appState.reader.readtext(crop, detail=0, paragraph=True, x_ths=0.5)
    print("Scanned!")
    #print("Recognized: ", listOfItems)

    if len(listOfItems) == 0:
        print("No drops detected! Make sure your enabling scanning when the drops appear on the screen!")
    else:
        queryPlatPrices(listOfItems)
        
    appState.screenshottingEnabled = 0