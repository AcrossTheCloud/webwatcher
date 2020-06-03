#!/usr/bin/env python3

import time
import urllib
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage

hostnames = []

with open('hostnames.txt','r') as hostnames_file:
  for line in hostnames_file:
    hostnames.append(line.rstrip())

while True:
    for hostname in hostnames:
      status = urllib.urlopen('https://'+hostname).getcode()

      if status != 200:
        msg = EmailMessage()
        msg.set_content('host ' + hostname + ' is down')

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'host ' + hostname + ' is down'
        msg['From'] = 'email@example.net'
        msg['To'] = 'email@example.net'

        # Send the message via our own SMTP server.
        s = smtplib.SMTP('server')
        s.send_message(msg)
        s.quit()
        
    #The number of seconds the loop will pause for before checking again.
    time.sleep(1800)