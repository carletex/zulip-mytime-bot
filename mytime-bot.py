#!/usr/bin/env python

import zulip
import sys

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

def hs_auth():


def respond(msg):

    content = msg['content'].upper().split()

    if ((content[0] == "MYTIME")
        or (content[0] == "@**MYTIME" and content[1] == "BOT**" and content[2] == "MYTIME")):
    	# Bot called
    	# 1 - Get user info (mail or batch + name? Depends os HS API)
    	# 2 - Get info from HS
    	# 3 - Get time
    	# 4 - Send message
    	pass

client.send_message({
    "type": "private",
    "to": "oceanrdn@gmail.com",
    "content": "Private text from mytime-bot"
})

# Print each message the user receives
# This is a blocking call that will run forever
client.call_on_each_message(lambda msg: sys.stdout.write(str(msg) + "\n"))