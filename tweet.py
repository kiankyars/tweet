import os
import tweepy
import sys

consumer_key = os.environ.get('TWEEPY_CONSUMER_KEY')
consumer_secret = os.environ.get('TWEEPY_CONSUMER_SECRET')
access_token = os.environ.get('TWEEPY_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWEEPY_ACCESS_TOKEN_SECRET')

def main():
    if len(sys.argv) < 2:
        print('Usage: python tweet.py "your tweet"')
        sys.exit(1)
    tweet = sys.argv[1]
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(tweet)
    print('Tweeted!')

if __name__ == '__main__':
    main() 