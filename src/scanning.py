from utility import itemToSlug
from apiHandler import getItemRequest
from colorama import Fore
import pytesseract

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
            
            dictOrders = getItemRequest(itemSlug)

            if type(dictOrders) == list:
                avgPlat = getAveragePlat(dictOrders)
            
                latestPlat = dictOrders[0]['platinum']

                print(Fore.CYAN + f"\t AVERAGE PLATINUM LISTING: " + Fore.RESET +  f"{avgPlat}p")
                print(Fore.CYAN + f"\t LATEST PLATINUM LISTING: " + Fore.RESET +  f"{latestPlat}p")
            else:
                print(f"Something went wrong while querying this item. API returned with status code: {dictOrders}")

    

def scanScreenshot(appState, crop):
    print("Now scanning...")
    listOfItems = pytesseract.image_to_string(crop, config='--psm 12')
    parsedItems = listOfItems.split('\n')
    print("Scanned!")
    #print("Recognized: ", listOfItems)

    if len(parsedItems) == 0:
        print("No drops detected! Make sure your enabling scanning when the drops appear on the screen!")
    else:
        print("Drops detected! Heres what Tesseract detected:")
        print(parsedItems)
        #queryPlatPrices(listOfItems)

    appState.screenshottingEnabled = 0