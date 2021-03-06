import json
import random
import sys
import textwrap
from pprint import pprint
from datetime import date, timedelta
from PIL import Image, ImageDraw, ImageFont

# Twitter header
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

def write_tweet(date, tweet, rotate):
    image = Image.new('RGBA', (1550, 1100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    # Draw border
    # draw.rectangle([(1, 1), (1549, 1099)], fill=None, outline='black')

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

    for line in lines:
        _, height = tweet_body_font.getsize(line)
        draw.text((x_text, y_text), line, fill=colour_body, font=tweet_body_font)
        y_text += height

    # Add avatar (assumes the image is circular)
    avatar = Image.open('avatar.png')
    avatar.thumbnail((180, 180))
    image.paste(avatar, (112, y_start + 290))

    # Rotate image (if necessary)
    if rotate:
        image = image.rotate(180)

    # Save image
    filename = date.strftime('%Y-%m-%d')
    print('Saving {}...'.format(filename))
    image.save('images/{}.png'.format(filename))

if __name__ == "__main__":
    verbose = 'verbose' in sys.argv
    # Can rotate image to aid in printing margins
    # Theory being that if you are printing 4 tweets on a single A4 page, this
    # will help the margins be more consistent
    rotate_image = 'rotate' in sys.argv

    count = 0
    rotate = False
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

            write_tweet(date, tweet['full_text'], rotate)
            if rotate_image:
                rotate = not rotate
            date += delta

    print('Done!')
    if verbose:
        print('Count: {}'.format(count))
