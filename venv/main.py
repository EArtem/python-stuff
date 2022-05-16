import smtplib
import datetime as dt
import pandas as pd
import random
import os
import fileinput
PASSWORD = 'it_is_a_secret'
TEMPLATES_FOLDER = 'letter_templates/'
SENDER_EMAIL = 'yartemtest@gmail.com'


now = dt.datetime.now()


df = pd.read_csv('birthdays.csv')
# list of users to send mail
mailing_list = {row['name']: row.email for (i, row) in df.iterrows() if (row.day == now.day and row.month == now.month)}

print(mailing_list)
print(len(mailing_list))


def email_data_generator(birthday_persons: dict):

    email_data = {}

    for name in birthday_persons:
        path_to_ranndom_template = 'letter_templates/' + random.choice(os.listdir('letter_templates/'))
        ranndom_template = open(path_to_ranndom_template, 'r')
        letter_to_send = ranndom_template.read().replace('[NAME]', name)
        ranndom_template.close()
        email_data.update({birthday_persons[name]: letter_to_send})

    return email_data


def send_emails(data: dict):
    count_emails = 0
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)

        for email_address, email_body in data.items():
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=email_address,
                                msg=email_body)
            count_emails += 1

    connection.close()
    print(f'emails sent: {count_emails}')


if len(mailing_list) > 0:
    email_data = email_data_generator(mailing_list)
    send_emails(email_data)




