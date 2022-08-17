# TODO: set up birthdays in csv file and set code to read csv
# TODO: set up crontab for script in cronjobs

import random
import email_send
import datetime
import requests

def get_kanye_quote():
    connection_kanye = requests.get('https://api.kanye.rest')
    connection_kanye.raise_for_status()
    kanye_data = connection_kanye.json()
    kanye_quote = kanye_data['quote']
    return kanye_quote


with open('quotes.txt', 'r') as f:
    quote_list = f.readlines()

inspirational_quote = random.choice(quote_list)
kanye_quote = get_kanye_quote()

message_text = f'Inspirational Quote: {inspirational_quote}\n<br>' \
               f'Kanye Quote: {kanye_quote}'

email_send.sendmail_text_only('Daily Quotes', ['matthewwillis55@yahoo.com', 'alejandravwillis@gmail.com'], message_text)

month_day = datetime.datetime.now().strftime("%m-%d")

birthday_dict = {'12-11': ['alejandracvc2@gmail.com', 'My Beautiful Wife Alejandra'], '10-12': ["matthewwillis55@gmail.com", "Matthew"]}

if month_day in birthday_dict.keys():
    birthday_recipients = birthday_dict[month_day]
    for recipient in birthday_recipients:
        print(recipient[0])
        subject = 'HAPPY BIRTHDAYYYYY'
        email_message = f'Happy Birthday {recipient[1]}!   -Matthew'
        tolist = [recipient[0]]
        email_send.sendmail_text_only(subject, tolist, email_message)




