import json
import tweepy
import csv

def cleanTweet(tweet):
  tweet = tweet.lower()
  tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
  tweet = re.sub('@[^\s]+','AT_USER',tweet)
  tweet = re.sub('[\s]+', ' ', tweet)
  tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
  tweet = tweet.strip('\'"')
  return tweet

# Enter your keys/secrets as strings in the following fields
consumer_key = "uRmhYow4fOoI1C6NrHd2hTRyE"  
consumer_secret = "YGTUR6sQyijpP8Vu5dhNIAEJTt88wJaklEdWtqxl1AYUUCwKJl"  
access_key = "908013362801401856-ZZMgepM0JVWpeNYRnuN9P0tTetXymOE"  
access_secret = "eyOgN7WB6Gtxwl2u8mqZ1XlhvboG2lddl4rBY8mUmlCJQ"

def get_tweets(username):
	#initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	tweetList = []	
	
	#get tweet from a username
	tweets = api.user_timeline(screen_name = username ,count=5, include_rts = True)
	
	for tweet in tweets:
		print(tweet.text)

if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_tweets("RestuWahyuKart1")