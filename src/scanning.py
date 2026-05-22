from utility import itemToSlug
from apiHandler import getRequest
from colorama import Fore
import keyboard

def getAveragePlat(dictOrders):
    totalPlat = 0

    for order in dictOrders:
        totalPlat += order['platinum']

    averagePlat = totalPlat / 5
    return averagePlat

def queryPlatPrices(listOfItems):
    for item in listOfItems:
        if item == "Forma Blueprint":
            print(Fore.RED + "\nForma Blueprint :(" + Fore.RESET)
        else:
            itemSlug = itemToSlug(item)
            #print(f"\n Item slug generated: {itemSlug}. Now querying warframe.market...")
            
            dictOrders = getRequest(itemSlug)

            if type(dictOrders) == list:
                avgPlat = getAveragePlat(dictOrders)
            
                latestPlat = dictOrders[0]['platinum']

                print(item.upper())
                print(Fore.CYAN + f"\t AVERAGE PLATINUM LISTING: " + Fore.RESET +  f"{avgPlat}p")
                print(Fore.CYAN + f"\t LATEST PLATINUM LISTING: " + Fore.RESET +  f"{latestPlat}p")
            else:
                print(f"Something went wrong while querying this item. API returned with status code: {dictOrders}")

    

def scanScreenshot(appState, crop):
    print("Now scanning screenshot...")
    listOfItems = appState.reader.readtext(crop, detail = 0)
    print("Screenshot scanned!")
    #print("Recognized: ", listOfItems)

    if len(listOfItems) > 4 or len(listOfItems) == 0:
        print("No drops detected! Make sure your enabling scanning when the drops appear on the screen!")
    else:
        queryPlatPrices(listOfItems)

    appState.screenshottingEnabled = 0