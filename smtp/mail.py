import os, sendgrid, reader
from sendgrid.helpers.mail import *

EMAIL_FROM = Email('aacpspcgrades@gmail.com')

def get_key():
    f = open(os.path.join(os.path.dirname(__file__), 'API_KEY.txt'))
    API_KEY = f.readline().rstrip()
    f.close()
    return API_KEY

def create_client(API_KEY):
    return sendgrid.SendGridAPIClient(apikey=API_KEY)

def create_message(EMAIL_TO, subject, content):
    to = Email(EMAIL_TO)
    c = Content('text/html', content)
    message = sendgrid.helpers.mail.Mail(EMAIL_FROM, subject, to, c)
    return message
