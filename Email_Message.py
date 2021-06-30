#Email_Message.py
#Sends an email with a given subject, body content to a specificed receiver's email address from stockalertpy@gmail.com

import smtplib
import email
from email.message import EmailMessage
from email.mime.text import MIMEText

class Email_Message:
    def __init__(self, subject, body, to):
        self.subject = subject
        self.body = body
        self.to = to
    
    def email_alert(self):
        msg = EmailMessage() #create an EmailMessage
        html = MIMEText(self.body, 'html') #set the text type to html
        msg.set_content(self.body)
        msg.add_alternative(self.body, subtype = "html")
        msg["Subject"] = self.subject #set subject
        msg["To"] = self.to #set receiver's email address

        user = "stockalertpy@gmail.com"
        msg["from"] = user

        password = "favtA1-tebcyr-vefsuw"
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587) #set up the SMTP server
            server.starttls()
            server.login(user, password)
            server.sendmail(user, self.to, msg.as_string()) #send email
            print("Email sent!")
        except:
           print ("Error: unable to send email")

        server.quit()
