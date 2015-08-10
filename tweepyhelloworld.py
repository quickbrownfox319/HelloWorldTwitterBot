#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, yaml

 
argfile = str(sys.argv[1])
 
with open('api_key.yml', 'r') as txt:
	key = yaml.load(txt)

consumer_key = key['consumer_key']
consumer_secret = key['consumer_secret']
access_token = key['access_token']
access_secret = key['access_secret']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(status=line)
    time.sleep(900)#Tweet every 15 minutes