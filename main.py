##################### Extra Hard Starting Project ######################
import smtplib

import pandas as pd
import datetime
import random
# 1. Update the birthdays.csv
all_birthdays=pd.read_csv('birthdays.csv')
dic=all_birthdays.to_dict(orient='records')
print(dic)


# 2. Check if today matches a birthday in the birthdays.csv
now=datetime.datetime.now()
print(now)
day=now.day
print(day)
month=now.month
print(month)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter1='./letter_templates/letter_1.txt'
letter2='./letter_templates/letter_2.txt'
letter3='./letter_templates/letter_3.txt'
letters=[letter1,letter2,letter3]

random_letter=random.choice(letters)
with open(random_letter) as file:
    file_content=file.read()


def email_message():
    for person in dic:
        if person['month'] == month and person['day'] == day:
            new_email=file_content.replace('[NAME]',person['name'])
            print(new_email)





# 4. Send the letter generated in step 3 to that person's email address.

mail_server='smtp.gmail.com'
password='jtqe jitx jadk deui'
email='georgehuffingtons@gmail.com'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,
                        to_addrs=email,
                        msg=f"Subject:Happy Birthday\n\n{email_message()}")





