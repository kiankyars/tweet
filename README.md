# Tweepy CLI

## Setup

Add these to your `~/.zshrc`:

```
export TWEEPY_CONSUMER_KEY="<your_consumer_key>"
export TWEEPY_CONSUMER_SECRET="<your_consumer_secret>"
export TWEEPY_ACCESS_TOKEN="<your_access_token>"
export TWEEPY_ACCESS_TOKEN_SECRET="<your_access_token_secret>"
```

## Usage

```sh
cd ~/Code/tweepy_cli
source .venv/bin/activate
python tweet.py "your tweet here"
```

## Note

Requires `TWEEPY_BEARER_TOKEN` in environment for v2 posting. 