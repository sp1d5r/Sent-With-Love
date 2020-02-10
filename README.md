# Sent-With-Love

This is a program I decided to make for my girlfriend to cheer her up. As of right now i'm not sure what it does but we will see!!!! //TODO...

## Content
* [History](#history)
* [Breaking the problem down](#breaking-the-problem-down)
* [Solving the sub-problems](#solving-the-sub-problems)
  * [Sending an Email using Python](#sending-an-email-using-python)
  * [Getting the Messages to Send](#getting-the-messages-to-send)
  * [Getting the Replies](#getting-the-replies)
  * [Keeping the Program Running](#keeping-the-program-running)

## History 
This program was designed to send loving emails, at random intervals throughout the year to family/significant people in my life. I want to build this because I think a random email from someone you care about reminding you how much they care about you can have a positive impact on the rest of your day. As a computer scientist this is a piece of software i can develop (with hopefully not too much difficulty) and make my circle a tiny bit more positive.

## Breaking the Problem Down
Breaking down the problem we can see there are a few sub-problems which should each be solved before trying to create a final solution. Hopefully my solution can solve the following sub problems:
* [Sending an Email using Python](#sending-an-email-using-python)
* [Getting the Messages to Send](#getting-the-messages-to-send)
* [Getting the Replies](#getting-the-replies)
* [Keeping the Program Running](#keeping-the-program-running)

## Solving the Sub-Problems
### Sending an Email using Python
A quick overview of how computers send emails. Computers use the Simple Mail Transfer Protocol (SMTP) to send emails. 
It is a protocol which handles sending and routing e-mails between mail servers. 

Looking around we can discover there is a python module called [smtplib](https://docs.python.org/3/library/smtplib.html) 
which defines an SMTP client session object. This object can be used to send emails to any internet machine with an SMTP 
or ESMTP listerner daemon.

Here is a simple syntax to create one SMTP object, which can later be used to send an e-mail.

```python
import smtplib

# host = This is the host running your SMTP server
# port =  If you are providing host argument, then you need to specify a port, where SMTP server is listening. 
# Usually this port would be 25.
# local_username = If your SMTP server is running on your local machine, then you can specify just localhost as of this option.

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
```

Since i will be using my gmail account my section will look more  like  this:
```python
import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
except:
    print('Something went wrong...')
```

It's important to know that there will not be a secure connection when transferring the email. Although this isn't ideal
it shouldn't be too important since i will not use it to send any important information. 

Since i want to use my gmail account to send the emails i will need to allow python access to my gmail account.
Here are the steps required in sending emails:
1. Allow less secure apps to access account
2. if you have 2-step verification then you will need to create an app-specific password for less secure accounts,
3. Is you get an SMTPAuthenticationError with error code of 534, then add captcha for the program.

As for the actual Python code, all you need to do is call the login method: 
```python
import smtplib

gmail_user = 'you@gmail.com'
gmail_password = 'P@ssword!'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:
    print('Something went wrong...')

```

### Getting the Messages to Send
There are a few ways of getting the messages to send
1. I could write out a list of messages to send with their bodies and update this whenver.
2. I could get an email retriever. So whenever i send my account an email with body and subject, it takes it and adds 
it to the existing database. 

The second solution is more reasonable since I will not always have access to my computer and it's inconvient to have to 
wait before updating the database. 

Firstly i need to be able to get the emails, this involves using the gmail API. 
To use the gmail API there are two required steps:
- Turn on the Gmail API,
- Install the Google Client Library

Once you have the google client library installed you need to get two sets of json files:
1. credentials.json (this will be obtained from the getting the client library)
2. token.json (this will be obtained from running a script from the quickstart guide for google)

Now I will parse my email account for messages from myself/ messages with a specific subject.
The code can be found in the [corresponding python file](get_emails.py)

### Getting the Replies
This will be similar to the sub problem mentioned before, the only difference is this queries the reply.
This part would not be hard to do but, I cannot see any reason for doing this since I check my emails regularly
and I will be able to see the replies from my personal machine.


### Keeping the Program Running
Before I can deploy the python script i need to make a main class so it can complete all the tasks without me 
having to be there. This main class will take care of errors, randomly allocating the emails. and other things.

It seems important to specify what this main file will do:
* Get random intervals to send emails
* send those emails
* update the csv file to change the send parameter to true after sending the email
* Check if there are any more emails to add to the csv file 
* Catch any errors and notify me


talk about a requirements.txt file 

use heroku to keep the python script running indefinitely... 


## Helpful Links
*[GMail API quickstart](https://developers.google.com/gmail/api/quickstart/python)
*[Fetching E-mails Geeks for Geeks](https://www.geeksforgeeks.org/python-fetch-your-gmail-emails-from-a-particular-user/)
*[Deploying to Heroku help](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#set-up )