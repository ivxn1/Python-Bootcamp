##################### Hard Starting Project ######################
import random
import smtplib
import pandas
import datetime

my_email = 'ivxn.zhelev@gmail.com'
password = 'icrlgbgthmuwasrs'

birthday_data = pandas.read_csv("./birthdays.csv")
birthday_dictionary = pandas.DataFrame.to_dict(birthday_data, orient='records')

current_day = datetime.datetime.now().day
current_month = datetime.datetime.now().month

for p in birthday_dictionary:
    if p['day'] == current_day and p['month'] == current_month:

        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", 'r') as file:
            message = file.read()
            message = message.replace('[NAME]', p['name'])

        with smtplib.SMTP(host='smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=p['email'],
                msg=f'Subject:Happy Birthday!!!\n\n{message}'
            )

