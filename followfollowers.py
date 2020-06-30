import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys.py to see the format.
from keys import *

# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
#print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def follow_followers():
	mentions = api.mentions_timeline(tweet_mode='extended')
	for follower in tweepy.Cursor(api.followers).items():
		if not follower.following:
			print(f"Following {follower.name}")
			follower.follow()                   

while True:
    follow_followers()
    time.sleep(15)