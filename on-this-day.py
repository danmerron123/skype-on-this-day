import os
import sqlite3
import smtplib
from email.mime.text import MIMEText


conn = sqlite3.connect('/Users/danmerron/Library/Application Support/Skype/danmerron1/main.db')
c = conn.cursor()
rows = c.execute("select datetime(timestamp, 'unixepoch') as date,author,body_xml,convo_id from messages where convo_id = '1009' and date like '2016-12-15 %'")

f = open('out.txt', 'w')
for row in rows:
        alldemtings = c.fetchone()
        print alldemtings
        print >> f, alldemtings

fp = open('out.txt', 'rb')
TEXT = MIMEText(fp.read())
fp.close()

FROM = 'skype@onthisday.co.uk'
TO = ["danmerron@gmail.com"] # must be a list
SUBJECT = "Skype On This Day Premium"

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
username = 'danmerron@gmail.com'
password = '3mailSecure!'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(FROM, TO, message)
server.quit()


os.remove("out.txt")