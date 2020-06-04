#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()

import time
import requests
import smtplib
import os
# Import the email modules we'll need
from email.message import EmailMessage

hostnames = []

with open('hostnames.txt','r') as hostnames_file:
  for line in hostnames_file:
    hostnames.append(line.rstrip())

while True:
    for hostname in hostnames:
      try:
        status = requests.get('https://'+hostname).status_code

        if status != 200:
          msg = EmailMessage()
          msg.set_content('host ' + hostname + ' is down')

          # me == the sender's email address
          # you == the recipient's email address
          msg['Subject'] = 'host ' + hostname + ' is down'
          msg['From'] = 'matthew@acrossthecloud.net'
          msg['To'] = 'matthew@acrossthecloud.net'

          # Send the message via our own SMTP server.
          s = smtplib.SMTP('acrossthecloud-net.mail.protection.outlook.com')
          s.send_message(msg)
          s.quit()
      except Exception as e:
          msg = EmailMessage()
          msg.set_content('host ' + hostname + ' is down with exception {}'.format(e))

          # me == the sender's email address
          # you == the recipient's email address
          msg['Subject'] = 'host ' + hostname + ' is down'
          msg['From'] = os.getenv('EMAIL')
          msg['To'] = os.getenv('EMAIL')

          # Send the message via our own SMTP server.
          s = smtplib.SMTP(os.getenv('SMTPSERVER'))
          s.send_message(msg)
          s.quit()

        
    #The number of seconds the loop will pause for before checking again.
    time.sleep(1800)