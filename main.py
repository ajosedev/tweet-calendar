import json
import random
import sys
from pprint import pprint

# Quote of the day calendar

# Iterate over every tweet
# Ignore tweets with links in them?

# Create a page (in a pdf?) with a single tweet
#   Have different templates
# Show date (e.g. Jan 01)
# Figure out design for screen

if __name__ == "__main__":
    verbose = 'verbose' in sys.argv
    count = 0
    with open('tweets.json') as f:
        tweets = json.load(f)
        # Shuffle tweets into random order
        random.shuffle(tweets)

        for tweet in tweets:

            # Take out links
            if 'http' in tweet['full_text']:
                continue

            # Take out quotes
            if tweet['is_quote_status']:
                continue

            # Double check for links and images and such
            if tweet['entities']['urls'] or 'media' in tweet['entities']:
                continue

            # Take out replies
            if tweet['in_reply_to_status_id'] is not None:
                continue

            print(tweet['full_text'])
            count += 1

        if verbose:
            print('Count: {}'.format(count))
