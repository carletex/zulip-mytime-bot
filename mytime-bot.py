#!/usr/bin/env python

import zulip
import sys
from credentials import *
from hs_oauth import get_access_token, get_hs_credentials, request

HS_BASE_URL = 'https://www.hackerschool.com/api/v1'
username, password = get_hs_credentials()
access_token, refresh_token = get_access_token(username=username, password=password)
print 'token received'

# Subscriptions
f = open('subscriptions.txt', 'r')

ZULIP_STREAMS = []

try:
    for line in f:
        ZULIP_STREAMS.append(line.strip())
finally:
    f.close()

# Zulip Auth
client = zulip.Client(email = access['email'],
                      api_key = access['api_key'])

# client.add_subscriptions([{"name": stream_name} for stream_name in ZULIP_STREAMS])

def get_hs_person_info(sender_email):
    # 1 - Get person info: request /people/:email
    person = request(access_token, HS_BASE_URL + '/people/me')
    # 2 - Return the person
    return person

def get_time_diff(end_date):
    # ToDo
    return end_date


def process_message(msg):

    content = msg['content'].upper().split()

    if ((content[0] == "MYTIME")
        or (content[0] == "@**MYTIME" and content[1] == "BOT**" and content[2] == "MYTIME")):
        # Bot called
        # 1 - Get user's email
    	sender_email = msg['sender_email']

        # 2 - Get info from HS
        person = get_hs_person_info(sender_email)

        # 3 - Get time
        time_left = get_time_diff(person['batch']['end_date'])

        # 4 - Send message
        print msg
        client.send_message({
            "type": "private",
            "to": "oceanrdn@gmail.com",
            "content": "You have " + time_left +" days left in HackerSchool."
        })


# Print each message the user receives
# This is a blocking call that will run forever
client.call_on_each_message(process_message)