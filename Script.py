#Stock portfolio updater
#By Martin Cai

#This program extracts the data of a user's stock portfolio and emails them an update of their portfolio
#every time the program is called (or every weekday at 1:30 PST when the market closes).

import datetime
from CurrencyConverter import *
from Email_Message import *
from StockPrice import *
from tabulate import tabulate

stocks = {}
bodyHTML = "" #HTML text to be sent in the email
bodyPlainText = "" #plain text to be printed in the console
tabulate.PRESERVE_WHITESPACE = True

with open("/Users/martincai/Documents/Programming/Stock/stocks.txt") as file:
    for line in file:
        (key, val) = line.strip().split() #parse data from text file
        stocks[key] = val #set up a dictionary with stock names and the quantities

def getStockPrices(stocks):
    info = []
    for key in stocks:
        stockPrice = StockPrice(key).getStockPrice(2) #call StockPrice to get a stock's price in USD
        cadStockPrice = CurrencyConverter(stockPrice, "USD", "CAD").convert(2) #call CurrencyConverter to get corresponding CAD value
        quantity = int(stocks[key])
        totalPrice = round(cadStockPrice * quantity, 2)
        info.append([key, cadStockPrice, quantity, totalPrice]) #add all the data to an array 
    return info

def formatMessage(info):
    #both HTML and Plain text messages are stored because tables stored in plain text don't format well over emails

    bodyHTML = "<p> Stock portfolio update for {}\n\n <p>".format(datetime.datetime.now().strftime("%A, %b %d, %Y"))
    bodyPlainText = "Stock portfolio update for {}\n\n".format(datetime.datetime.now().strftime("%A, %b %d, %Y"))

    totalPrice = 0
    for line in info:
        totalPrice += line[3] #calculate total portfolio price

    #tabulate library is used to create the tables
    bodyHTML += tabulate(info, headers = ["Stock Name,", "Price (CAD)", ", Quantity", ", Total Price (CAD)"], floatfmt=".2f", numalign="right", tablefmt="html")
    bodyPlainText += tabulate(info, headers = ["Stock Name", "Price", "Quantity", "Total Price"], floatfmt=".2f", numalign="right")

    bodyHTML += "<p> Total portfolio value: ${:.2f} CAD <p>".format((totalPrice))
    bodyPlainText += "\n\nTotal portfolio value: ${:.2f} CAD".format((totalPrice))

    print(bodyPlainText)
    return bodyHTML

def main():
    subject = "Current portfolio value for {}".format(datetime.datetime.now().strftime("%A, %b %d, %Y"))
    body = formatMessage(getStockPrices(stocks))
    to = "sampleaddress@gmail.com" #replace with your email address
    Email_Message(subject, body, to).email_alert() #send email through the EmailMessage.py program
    return

if __name__ == '__main__':
    main()

#cron code used to run the program on a user's computer every weekday when the market closes
#replace with the location of the Script.py file
#PST:
#30 13 * * 1-5 /usr/local/bin/python3 *location of Script.py on your computer*
#EST:
#30 16 * * 1-5 /usr/local/bin/python3 *location of Script.py on your computer*
