import os
import tweepy

def tweet(text):
    bearer_token = os.environ.get('TWEEPY_BEARER_TOKEN')
    consumer_key = os.environ.get('TWEEPY_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWEEPY_CONSUMER_SECRET')
    access_token = os.environ.get('TWEEPY_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWEEPY_ACCESS_TOKEN_SECRET')
    if not all([bearer_token, consumer_key, consumer_secret, access_token, access_token_secret]):
        raise RuntimeError('Missing Twitter API keys. See the README for setup instructions.')
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    client.create_tweet(text=text)
