import os
import tweepy
import sys

bearer_token = os.environ.get('TWEEPY_BEARER_TOKEN')
consumer_key = os.environ.get('TWEEPY_CONSUMER_KEY')
consumer_secret = os.environ.get('TWEEPY_CONSUMER_SECRET')
access_token = os.environ.get('TWEEPY_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWEEPY_ACCESS_TOKEN_SECRET')

def main():
    if len(sys.argv) < 2:
        print('Usage: uv run tweet.py "your tweet"')
        sys.exit(1)
    tweet = sys.argv[1]
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    client.create_tweet(text=tweet)

if __name__ == '__main__':
    main() 