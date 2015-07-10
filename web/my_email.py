import smtplib


s = smtplib.SMTP("Smtp.1and1.com")
senderMail = "c1122@cs.hku.hk"
recipientMail = "boyuwei@gmail.com"

message="Subject: This is the subject\r\n"
message += "From : Anybody <anybody@cs.hku.hk>\r\n"
message += "To : Anybody <anybody@cs.hku.hk>\r\n"
message += """Hello!
I am going to treat you a big meal!
"""


print "Sending mail...", s.sendmail(senderMail, recipientMail, message)
print "Done!"

s.quit()
