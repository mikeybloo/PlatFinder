import requests
import json

BASE_URL = 'https://api.warframe.market/v2'

def getRequest(itemSlug):
    global BASE_URL
    response = requests.get(f'{BASE_URL}/orders/item/{itemSlug}/top')
    dictResponse = deserializeJSON(response.text)
    
    return dictResponse['data']['sell']

def deserializeJSON(jsonString):
    return json.loads(jsonString)