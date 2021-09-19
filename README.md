
# Stock Portfolio Updater

Hi! Stock Portfolio Updater is a program that extracts the data of a user's stock portfolio and emails them an update of their portfolio every time the program is called (or every weekday when the stock market closes). The update shows the stock names, their individual prices in CAD, quantity owned, and the total price of each stock and the entire portfolio in CAD.

## Installation

1. Clone the repository into your IDE of choice.
2. Replace the sample stock names and quantities with your own information in the format "stockName stockQuantity".
3. Install the necessary libraries using:
```bash
pip install yahoo-fin requests tabulate
```
4. On line 56 of Script.py, replace "sampleaddress@gmail.com" with your own email address.
5. If needed to protect confidentiality, you can create your own email address to send your updates through. Open EmailMessage.py and replace the ```user``` and ```password``` values with your own. If using gmail, make sure to allow access for less secure apps. 
[Link.](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjej_aJh7nxAhWLjp4KHU6LBpQQFjAAegQICRAD&url=https%3A%2F%2Fsupport.google.com%2Faccounts%2Fanswer%2F6010255%3Fhl%3Den&usg=AOvVaw3-1FTJa5q6A7ZR_7SeNfng)
6. If you have turned HTML emails off, please turn them on before running this program!

## Usage
Once everything is set up, run the Script.py file. To run the script every weekday when the market closes at 1:30 PST, use cron in the terminal to allow for the script to run automatically.
```bash 
crontab -e
```
Press "i" and "enter". Then, copy one of the commands at the bottom of the Script.py file depending on your time zone. Replace the last part with the locations of python3 and the the Script.py file on your computer. This is an example command:
```bash
30 13 * * 1-5 /usr/local/bin/python3 /Users/martin/Documents/Programming/Stock/Script.py
```
Press ESC and then type in ":wq" to save your changes. To delete the cron job, type in:
```bash
crontab -r
```

## Future contributions
I originally used the tabulate library to create a nicely formatted table that displayed all the information in a clear manner. However, the table was stored in plain text and the formatting did not translate well during the email sending process. Instead, I had to use tabulate to create a HTML table to send over email, which resulted in a slightly messier table. In the future, I hope to be able to either learn how to preserve the formatting of plain text over email or learn how to format the HTML table better.
