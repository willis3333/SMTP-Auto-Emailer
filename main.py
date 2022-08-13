# TODO: set up birthdays in csv file and set code to read csv

import random
import email_send
import datetime

with open('quotes.txt', 'r') as f:
    quote_list = f.readlines()

quote = random.choice(quote_list)

email_send.sendmail_text_only('Daily inspirational quote', ['matthewwillis55@yahoo.com', 'alejandravwillis@gmail.com'], quote)

month_day = datetime.datetime.now().strftime("%m-%d")

birthday_dict = {'08-11': [['alejandracvc2@gmail.com', 'My Beautiful Wife Alejandra'], ["matthewwillis55@yahoo.com", "Matthew"]]}

if month_day in birthday_dict.keys():
    birthday_recipients = birthday_dict[month_day]
    for recipient in birthday_recipients:
        print(recipient[0])
        subject = 'HAPPY BIRTHDAYYYYY'
        email_message = f'Happy Birthday {recipient[1]}!   -Matthew'
        tolist = [recipient[0]]
        email_send.sendmail_text_only(subject, tolist, email_message)




