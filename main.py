import get_emails
import send_email
import random
import time
import pandas as pd

SENDER = "almazahmd03@gmail.com"
RECIPIENTS = ["nadiaaliyah@gmail.com", "almazahmad03@gmail.com"]


def sending_email(msg):
    send_email.send_email(SENDER, RECIPIENTS, msg)


def send_admin_email(msg):
    send_email.send_email(SENDER, ["almazahmad03@gmail.com"], msg)


def run():
    # send Test Email
    sending_email("Nadia, Just to inform you Elijah Ahmad has uploaded the file \n " +
                  "prepare for intense loving sweetheart \n \n Yours forever, \n Elijah xx")

    while True:
        try:
            if check_emails_exist():
                # gets the next message to send
                message = get_message_sent()
                # sends the messages
                sending_email(message)

            # Regardless of if condition it goes to sleep.
            time.sleep(get_random_time())
            # updates the email list
            get_emails.get_emails(get_emails.test_query)

        except:
            send_admin_email("There's been a problem lol...")


def get_random_time():
    return random.randint(259200,804800)


def check_emails_exist():
    data = pd.read_csv(get_emails.csv_file_name + '.csv')
    unused_emails = data[data["Used"] == False]
    if unused_emails.empty():
        sending_email("update email mate...")
        return False
    return True


def get_message_sent():
    data = pd.read_csv(get_emails.csv_file_name+'.csv')
    unused_emails = data[data["Used"] == False]
    message = unused_emails["Message Body"].iat[0]
    data.loc[data['Message Body'] == message, 'Used'] = True
    data.to_csv(get_emails.csv_file_name+'.csv', index=False)

    return message

