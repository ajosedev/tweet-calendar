import json
import random
import sys
from pprint import pprint
from datetime import date, timedelta

# Quote of the day calendar

# Create a page (in a pdf?) with a single tweet
#   Have different templates
#   4 tweets per page

# Figure out design for screen

if __name__ == "__main__":
    verbose = 'verbose' in sys.argv

    count = 0
    year = 2019

    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    delta = timedelta(days=1)
    date = start_date

    with open('tweets.json') as f:
        # Load tweets from file
        tweets = json.load(f)
        # Shuffle tweets into random order
        random.shuffle(tweets)

        # Iterate over dates
        while date <= end_date:
            tweet = tweets[count]
            # Increment count after accessing tweet, incase tweet is unwanted
            # Count may increase without date increasing
            count += 1

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

            print('{} - {}'.format(date.strftime("%a, %d %b"), tweet['full_text']))
            date += delta

        if verbose:
            print('Count: {}'.format(count))
