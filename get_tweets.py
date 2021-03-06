import tweepy
import json
import secrets
from pprint import pprint

auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)
api = tweepy.API(auth)

twitter_handle = "dog_feelings"
count = 600

# Get a bunch of tweets for a given user
# Gets more than 365 tweets, as they are randomised and shuffled
# Saves tweets to a JSON file, as we do not need to constantly update them
if __name__ == "__main__":
    json_tweets = []

    for tweet in tweepy.Cursor(api.user_timeline, screen_name = twitter_handle, count = count, include_rts = False, tweet_mode = 'extended', trim_user = True).items(500):
        json_tweets.append(tweet._json)

    with open('tweets.json', 'w') as outfile:
        json.dump(json_tweets, outfile, sort_keys = True, indent = 2)
