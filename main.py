import json
import random
import sys
import textwrap
from pprint import pprint
from datetime import date, timedelta
from PIL import Image, ImageDraw, ImageFont

# Quote of the day calendar

# Create a page (in a pdf?) with a single tweet
#   4 tweets per page

# Copy
twitter_name = 'Thoughts of dog'
twitter_handle = 'dog_feelings'

# Fonts
date_num_font = ImageFont.truetype('/Users/andrew/Library/Fonts/Roboto-Black.ttf', 200)
date_day_font = ImageFont.truetype('/Users/andrew/Library/Fonts/Roboto-Bold.ttf', 80)
tweet_heading_font = ImageFont.truetype('/Users/andrew/Library/Fonts/Roboto-Bold.ttf', 60)
tweet_body_font = ImageFont.truetype('/Users/andrew/Library/Fonts/Roboto-Regular.ttf', 60)

# Colours
colour_date_num = (0, 0, 0)
colour_date_day = (128, 128, 128)
colour_user = (101, 119, 134)
colour_body = (20, 23, 26)

def write_tweet(date, tweet):
    avatar = Image.open('avatar.png')
    txt = Image.new('RGBA', (1400, 1000), (255, 255, 255, 0)) # Change this to 255, 255, 255, 0 when saving
    draw = ImageDraw.Draw(txt)
    draw.rectangle([(1, 1), (1399, 999)], fill=None, outline='black')

    # Set start 'margins'
    y_start = 60
    x_text = 330
    y_text = y_start + 360

    # Write date
    draw.text((80, y_start), date.strftime('%d'), fill=colour_date_num, font=date_num_font, align='right')
    draw.text((x_text, y_start + 30), date.strftime('%A'), fill=colour_date_day, font=date_day_font)
    draw.text((x_text, y_start + 110), date.strftime('%b'), fill=colour_date_day, font=date_day_font)

    # Write tweet header
    draw.text((x_text, y_start + 290), '{}'.format(twitter_name), fill=colour_body, font=tweet_heading_font)
    draw.text((790, y_start + 290), '@{}'.format(twitter_handle), fill=colour_user, font=tweet_body_font)

    # Write tweet content
    lines = textwrap.wrap(tweet, width=35)

    # TODO - handle when line length is too long (e.g. when all caps)
    for line in lines:
        _, height = tweet_body_font.getsize(line)
        draw.text((x_text, y_text), line, fill=colour_body, font=tweet_body_font)
        y_text += height

    # Save image
    print('Saving...')
    txt.paste(avatar, (84, y_start + 290)) # Assumes the avatar is styled correctly
    txt.save('images/{}.png'.format(date.strftime('%d-%m')))

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
        # while date <= end_date:
        while count <= 4:
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

            write_tweet(date, tweet['full_text'])
            date += delta

    if verbose:
        print('Count: {}'.format(count))
