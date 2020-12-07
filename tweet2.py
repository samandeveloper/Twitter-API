#In this project we are going to create a twiiter bot using Tweepy Library!!
import tweepy   #tweepy is an API for Twitter 
import time    # time is a module for sending request to tweepy

#add your developer twitter account in the following section (consumer_key,consumer_secret,access_token,access_token_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user=api.me()	#go to your twitter account 

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)

#we want to search inside tweets and if we see 'python' word, and like it for 2 times
search = 'python'
numberOfTweets = 2 # like 2 times
for tweet in tweepy.cursor(api.search,search).items(numberOfTweets):
	try:
		tweet.favorite()	#favorite two tweets with 'python' name
		tweet.retweet()		#retweet two tweets with 'python' name
		print('like that tweet')
	except tweepError as e:
		print(e.reason)
	except stopIteration:
		break



