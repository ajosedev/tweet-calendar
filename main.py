import json
from pprint import pprint

# Quote of the day calendar

# Given a user
# Get their last 365 tweets (pretend leap years dont exist)
# Save them to a JSON file

# Figure out how to shuffle
# Iterate over every tweet
# Ignore tweets with links in them

# Create a page (in a pdf?) with a single tweet
#   Have different templates

if __name__ == "__main__":
    with open('tweets.json') as f:
        count = 0
        data = json.load(f)
        for tweet in data:
            print(tweet['full_text'])
            count += 1
        print('count:', count)
