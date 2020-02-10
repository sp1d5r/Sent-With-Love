import smtplib
import config as pk


def send_email(sender, recipient, subject, body):
    """
    Params:
    sender = string, your email
    recipient = String[], or all users who get the message
    subject = string, subject of email
    body = string, body of the email
    """

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sender, ", ".join(recipient), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(pk.gmail_user, pk.gmail_password)
        server.sendmail(sender, recipient, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')



