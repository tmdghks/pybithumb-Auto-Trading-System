import requests

url = "https://api.upbit.com/v1/candles/days"

querystring = {"market":"KRW-ETH"}

response = requests.request("GET", url, params = querystring)

print(response.text)