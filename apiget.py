import requests as re
import json

# response = requests.get("http://api.open-notify.org/astros.json")
# rj = response.json()
# print(rj)
# print(rj['people'][0])
# # print(json.dumps(rj))

response = re.get("http://api.nbp.pl/api/exchangerates/rates/A/USD/")
print(response)

table = response.json()
print(table)
print(table['table'])
print(table['currency'])
print(table['code'])
print(table['rates'])
print(table['rates'][0])
print(table['rates'][0]['effectiveDate'])
print(table['rates'][0]['mid'])

