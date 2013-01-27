#!/usr/bin/python
import smtplib
import settings

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send(url):
    sender = settings.sender
    recipient = settings.recipient
    subject = 'Phone is available'
    body = "Click on this link %s" %url

    headers = [ "From: " + sender,
                "Subject: " + subject,
                "To: " + ', '.join(recipient),
                "MIME-Version: 1.0",
                "Content-Type: text/html"]

    headers = "\r\n".join(headers)

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, settings.password)

    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()
