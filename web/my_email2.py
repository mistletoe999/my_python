#!/usr/bin/python

import smtplib

sender = "boyuwei@gmail.com"
receivers = "boyuwei@gmail.com"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
#Next, log in to the server
s.login("boyuwei@gmail.com", "stwc1023_Gm")


message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
   s.sendmail(sender, receivers, message)
   print "Successfully sent email"
except:
   print "Error: unable to send email"
