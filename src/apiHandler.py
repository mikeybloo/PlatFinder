import requests
import json

BASE_URL = 'https://api.warframe.market/v2'

def getRequest(itemSlug):
    global BASE_URL
    response = requests.get(f'{BASE_URL}/orders/item/{itemSlug}/top')
    
    if response.status_code == 200:
        dictResponse = deserializeJSON(response.text)
    
        return dictResponse['data']['sell']
    else:
        return response.status_code

def deserializeJSON(jsonString):
    return json.loads(jsonString)