# twtr

## Setup

1. Make a free account and project at [developer.x.com](https://developer.x.com) and get the following keys:

- Bearer Token
- Consumer Key
- Consumer Secret
- Access Token
- Access Token Secret

![keys](keys.png)

2. Add your keys to your shell config

Add these lines to your `~/.zshrc` or `~/.bashrc`:
```sh
export TWEEPY_BEARER_TOKEN="<your_bearer_token>"
export TWEEPY_CONSUMER_KEY="<your_consumer_key>"
export TWEEPY_CONSUMER_SECRET="<your_consumer_secret>"
export TWEEPY_ACCESS_TOKEN="<your_access_token>"
export TWEEPY_ACCESS_TOKEN_SECRET="<your_access_token_secret>"
```
Then reload your config:
```sh
source ~/.zshrc # or source ~/.bashrc
```

## Usage

Install from PyPI with uv:

```sh
uv tool install twtr
```

Then tweet from the CLI:

```sh
twtr "your tweet here"
```