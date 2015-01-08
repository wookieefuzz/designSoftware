#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'RmO4nmsffvB1ceYCJhyoQFPiv'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '4zai09A04znldUbn4u1P7gtZjq1EkkFkiutKAB3z3Dy7YhKMIP'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '2720656262-PcrEE57Dp3zZfVav0oxppDZgdPsu3AY8QRoTPaL'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'QLpbx4JS1VkeogoN5mDP1NN4siEzfaEQ2Ww6Td152EIUp'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(30)#Tweet every 30 seconds
