#!/usr/bin/env python

import zulip
import sys
import time
import datetime
import math
import os
import urllib
from hs_oauth import get_access_token, request

TIME_UNITS = [('week', 7*24*60*60), ('day', 24*60*60), ('hour', 60*60), ('minute', 60), ('second', 1)]

def get_hs_person_info(sender_email):
    # 1 - Get person info: request /people/:email
    person = request(access_token, HS_BASE_URL + '/people/' + urllib.quote(sender_email))
    # 2 - Return the person
    return person

def get_time_diff(end_date, start_date = 0):
    ''' Get the formatted difference between two dates '''

    end_date = time.mktime(datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S").timetuple())
    if not start_date:
        start_date = time.strftime('%Y-%m-%d %H:%M:%S')

    start_date = time.mktime(datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S").timetuple())

    diff = abs(end_date - start_date)
    output = ''
    for unit in TIME_UNITS:
        division = diff / unit[1]
        if division >= 1:
            output += str(int(math.floor(division))) + ' ' + unit[0]
            if division >= 2:
                output += 's'
            output += ' '
            diff = diff % unit[1]

    return output.rstrip()


def process_message(msg):
    content = msg['content'].upper().split()

    if ((content[0] == "MYTIME")
        or (content[0] == "@**PRESSURE" and content[1] == "BOT**" and content[2] == "MYTIME")):
        # Bot called
        # 1 - Get user's email
    	sender_email = msg['sender_email']

        # 2 - Get info from HS
        person = get_hs_person_info(sender_email)

        # 3 - Get time
        hs_end_date = person['batch']['end_date'] + ' 18:30:00'
        time_left = get_time_diff(hs_end_date)

        # 4 - Send message
        print msg
        client.send_message({
            "type": "private",
            "to": msg['sender_email'],
            "content": "You have " + time_left +" left in HackerSchool."
        })


if __name__ == '__main__':

    # HS auth
    HS_BASE_URL = 'https://www.hackerschool.com/api/v1'

    username = os.environ.get('HS_LOGIN', None);
    password = os.environ.get('HS_PASS', None);
    access_token, refresh_token = get_access_token(username=username, password=password)

    print 'HS OAauth: access token received'
    print 'Listening to messages...'

    # Zulip Auth
    client = zulip.Client(email = os.environ.get('ZULIP_BOT_EMAIL', None),
                          api_key = os.environ.get('ZULIP_API_KEY', None))
    # Zulip subscriptions
    f = open('subscriptions.txt', 'r')
    ZULIP_STREAMS = []

    try:
        for line in f:
            ZULIP_STREAMS.append(line.strip())
    finally:
        f.close()

    client.add_subscriptions([{"name": stream_name} for stream_name in ZULIP_STREAMS])

    # Listening: This is a blocking call that will run forever
    client.call_on_each_message(process_message)