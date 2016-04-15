# coding: utf-8
import requests

# Configure your bot
TOKEN = 'YOUR TOKEN'
GROUPID =  #should be a negative number
method = 'sendMessage'


def bot(status):
    if status == 'checkin':  # check the param we get
        status = 'hapur'  # Translating into Albanian
    elif status == 'checkout':
        status = 'mbyllur'
    message = 'Open labs është {}.'.format(status)
    response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(TOKEN, method),
        data={'chat_id': GROUPID, 'text': message}
    ).json()
