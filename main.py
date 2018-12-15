import json
from pprint import pprint

# Quote of the day calendar

# Figure out how to shuffle
# Iterate over every tweet
# Ignore tweets with links in them?

# Create a page (in a pdf?) with a single tweet
#   Have different templates
# Show date (e.g. Jan 01)
# Figure out design for screen

if __name__ == "__main__":
    with open('tweets.json') as f:
        tweets = json.load(f)

        for tweet in tweets:
            print(tweet['full_text'])
