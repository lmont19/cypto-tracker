from configs import api_key, webhook_url
import requests
import json 
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

params = {'id': 52}
headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': api_key,
  }

request = requests.get(url, params=params, headers=headers)
request_json = request.json()
xrp_price = request_json['data']['52']['quote']['USD']['price']

print(xrp_price)

price = { 'value1': xrp_price}

requests.post(webhook_url, json=price)
