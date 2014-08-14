#!/usr/bin/env python

import zulip
import sys
import time
import datetime
import math
from credentials import *
from hs_oauth import get_access_token, get_hs_credentials, request

time_units = [('week', 7*24*60*60), ('day', 24*60*60), ('hour', 60*60), ('min', 60), ('second', 1)]


def get_hs_person_info(sender_email):
    # 1 - Get person info: request /people/:email
    person = request(access_token, HS_BASE_URL + '/people/me')
    # 2 - Return the person
    return person

def get_time_diff(end_date, start_date = 0):
    if not end_date:
        #
    end_date = time.mktime(datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S").timetuple())
    start_date = time.mktime(datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S").timetuple())
    diff = end_date - start_date
    output = ''
    for unit in time_units:
        number = diff / unit[1]
        if number >= 1:
            output += str(int(math.floor(number))) + ' ' + unit[0]
            if number >= 2:
                output += 's'
            output += ' '
            diff = diff % unit[1]

    return output


def process_message(msg):

    content = msg['content'].upper().split()

    if (msg['sender_email'] == 'oceanrdn@gmail.com') and ((content[0] == "MYTIME")
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


if __name__ == '__main__':
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
    client.add_subscriptions([{"name": stream_name} for stream_name in ZULIP_STREAMS])

    # Zulip Auth
    client = zulip.Client(email = access['email'],
                          api_key = access['api_key'])
    client.call_on_each_message(process_message)