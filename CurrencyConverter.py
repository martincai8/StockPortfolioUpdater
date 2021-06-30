#CurrencyConverter.py
#Fetches currency conversion data from the ExchangeRate API and converts an amount of money from USD to any other currency.
#Limitation: Since I am using the free plan from the ExchangeRate API, I only have access to 24 hour updates of exchange rates (they are not real-time).

import requests
import json
response = requests.get(url = ("https://v6.exchangerate-api.com/v6/7bae3436906b2b688ac2dc4d/latest/USD"))
data = response.json()


class CurrencyConverter:
    def __init__(self, amount, from_currency, to_currency):
        self.amount = amount
        self.from_currency = from_currency
        self.to_currency = to_currency


    def convert(self, digits):
        response = requests.get(url = ("https://v6.exchangerate-api.com/v6/2a1b6ec10e92e42c767328d5/latest/" + self.from_currency))
        data = response.json()

        exchange = data ['conversion_rates'] [self.to_currency] 
        price = self.amount * exchange

        return round(price, digits)
