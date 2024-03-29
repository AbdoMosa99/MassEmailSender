import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
import csv
import re
from time import sleep

from settings import *


print('Welcome to Multiple Mail Service!\n')
print('Please provide us with the needed informaion:')

# sender address
sender_address = SENDER_EMAIL
if not SENDER_EMAIL:
    sender_address = input('Sender Email Address: ')
    email_regex = '^(\w|\.)+@(\w+\.)+\w{2,4}$'
    if(not re.search(email_regex,sender_address)):
        print("Invalid Email Address! Aborting.")
        exit()

# sender password
sender_pass = getpass(prompt='Password: ')

# Create SMTP session for sending the mail
try:
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls() # enable security
    session.login(sender_address, sender_pass)
except Exception:
    print("Cannot login to Gmail! Aborting.")
    exit()

# email content
email_subject = SUBJECT if SUBJECT else input('Email Subject: ')
email_body_file_name = BODY_PATH if BODY_PATH else input('Email Body File: ')
try:
    email_body_file = open(email_body_file_name, "r")
except IOError:
    print(f"Cannot open {email_body_file_name}! Aborting.")
    exit()
else:
    email_body = email_body_file.read()
    email_body_file.close()

# dict from csv file of receivers
csv_file_name = RECEIVERS_PATH if RECEIVERS_PATH else input('CSV File for Receivers: ')
try:
    csv_file = open(csv_file_name, "r")
except IOError:
    print(f"Cannot open {csv_file_name}! Aborting.")
    exit()
else:
    receivers_dict = csv.DictReader(csv_file)

print("\nWorking...\n")

# prepare place holders
place_holder_regex = re.compile('%%\w+%%')
place_holders = place_holder_regex.findall(email_body)

# send mail to every receiver
for receiver in receivers_dict:
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['Subject'] = email_subject
    message['To'] = receiver_address = receiver["Email"]

    # prepare and attach body
    email_body_temp = (email_body + '.')[:-1]  # ? 
    for place_holder in place_holders:
        value = receiver[place_holder[2:-2]]
        email_body_temp = re.sub(place_holder, value, email_body_temp)
    message.attach(MIMEText(email_body_temp, 'html'))

    # send mail
    session.sendmail(sender_address, receiver_address, message.as_string())

    # print log
    print(f'Sent to {receiver_address}')
    sleep(1)

# finish
session.quit()
print('\nMission Completed Successfully.')
