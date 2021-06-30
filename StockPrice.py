#StockPrice.py
#Fetch live stock price data from the yahoo_fin python package and returns the price of an individual stock
#rounded to a given number of digits

from yahoo_fin import stock_info as si

class StockPrice:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def getStockPrice(self, digits):
        price = round(si.get_live_price(self.ticker), digits)
        return(price)
