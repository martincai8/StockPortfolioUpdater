#EmailMessage.py
#Given a subject, body content, and receiver email address, this program sends an email to the receiver's address from stockalertpy@gmail.com.

import smtplib
import email
from email.message import EmailMessage
from email.mime.text import MIMEText

class EmailMessage:
    def __init__(self, subject, body, to):
        self.subject = subject
        self.body = body
        self.to = to
    
    def email_alert(self):
        msg = EmailMessage()
        html = MIMEText(self.body, 'html')
        msg.set_content(self.body)
        msg.add_alternative(self.body, subtype = "html")
        msg["Subject"] = self.subject
        msg["To"] = self.to

        user = "stockalertpy@gmail.com"
        msg["from"] = user

        password = "favtA1-tebcyr-vefsuw"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.sendmail(user, self.to, msg.as_string())
        #print("Email sent!")
        #print ("Error: unable to send email")

        server.quit()
