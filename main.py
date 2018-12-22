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

twitter_name = 'dog_feelings'

font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 30)
font2 = ImageFont.truetype('/Library/Fonts/Arial Black.ttf', 100)
font3 = ImageFont.truetype('/Library/Fonts/Arial Black.ttf', 40)

def write_tweet(date, tweet):
    img = Image.new('RGB', (877, 620), 'white')
    draw = ImageDraw.Draw(img)

    # Set start 'margins'
    x_start = 100
    y_start = 80

    # Write date
    date_num = date.strftime('%d')
    draw.text((x_start, y_start), date_num, fill='black', font=font2)
    date_num_width, _ = draw.textsize(date_num, font=font2)
    draw.text((x_start + date_num_width, 100), date.strftime('%A'), fill='red', font=font3)
    draw.text((x_start + date_num_width, 145), date.strftime('%b'), fill='blue', font=font3)

    # Write tweet content
    x_text = x_start
    y_text = 250
    lines = textwrap.wrap(tweet, width=45)

    # TODO - handle when line length is too long (e.g. when all caps)
    for line in lines:
        _, height = font.getsize(line)
        draw.text((x_text, y_text), line, fill='black', font=font)
        y_text += height

    # Write author (hard coded)
    draw.text((x_start + 40, y_text + 40), '- @{}'.format(twitter_name), fill='green', font=font)

    # Save image
    print('Saving...')
    img.save('images/{}.png'.format(date.strftime('%d-%m')))

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
        while count <= 0:
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
