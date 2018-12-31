# tweet-calendar
Generates a 'word of the day' calendar, with a tweet for every day.

After scrolling through [@dog_feelings](https://twitter.com/dog_feelings/), my partner joked that she wanted a 'word of the day' calendar that
just contained tweets from the user. So, I made this for Christmas!

Tweets are obtained when running `get_tweets.py`, not part of the main function, as the tweets realistically only needed to be retrieved once.
More than the required amount (365) tweets are retrieved, as they are randomised when outputting the images.

## How to use
1. Create a `secrets.py` containing your Twitter developer account information (see what's needed in `get_tweets.py`)
2. Change the `twitter_handle` in `get_tweets.py` to your wanted Twitter handle
3. Change the `twitter_name` and `twitter_handle` in `main.py` also
3. Run `get_tweets.py` to create a `tweets.json` file
4. Run `main.py` to create the images - one image is created per day
  - The pixel placement is all absolute, and may need to be adjusted to better suit the selected Twitter user's name, handle, etc.
  - `rotate` can also be specified (i.e. `python main.py rotate`), to rotate in every second image. See notes for info.

## Notes
- Requires a Twitter developer account to obtain the tweets for a user
- Recommended: a paper guillotine, a hole punch, and to print 4 images per page - resulting in 365 A6-sized pages.
- The rotation flag may help to get achieve consistent margins on paper when cutting
- I don't know enough about print and resolutions, so the end result may not be _optimal_, but it looks perfect for its intended purpose.
