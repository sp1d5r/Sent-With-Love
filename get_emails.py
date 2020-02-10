from googleapiclient.discovery import build
from httplib2 import Http
import base64
import csv
import os
import pandas as pd
from oauth2client import file, client, tools

csv_file_name = "email"
update_message_subject = "I Love You"

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
test_query = ("\"subject:" + update_message_subject + "\"")


def get_emails(query):
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me', labelIds=['INBOX'],
                                              q=(query)).execute()
    messages = results.get('messages', [])
    for message in messages:
        # Add to csv File
        message = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
        update_csv(parse_msg(message))


def parse_msg(msg):
    if msg.get("payload").get("body").get("data"):
        return base64.urlsafe_b64decode(msg.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
    return msg.get("snippet")


def create_csv(msg):
    """
    :param msg: String, message you want to add to the csv file
    :return: null
    """
    with open((csv_file_name + '.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Message Body", "Used"])
        writer.writerow([msg, False])


def update_csv(msg):
    """
    :param msg: String, message you want to add
    :return: null
    """
    if os.path.exists(csv_file_name+'.csv'):
        data = pd.read_csv(csv_file_name + '.csv')
        unused_emails = data[data["Message Body"] == msg]
        if unused_emails.empty:
            new_row = pd.DataFrame({"Message Body": msg, "Used": False})
            data.append(new_row)
        else:
            print('Already Added MSG')
    else:
        create_csv(msg)

