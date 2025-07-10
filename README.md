# Tweet

## Setup

1. Make a free account and project at [developer.x.com](https://developer.x.com) and get the following keys:

- Bearer Token
- Consumer Key
- Consumer Secret
- Access Token
- Access Token Secret

![keys](keys.png)

2. Add your keys

- **Option 1: Use a `.env` file**

  ```sh
  cp .env.example .env
  ```

- **Option 2: Add to your `~/.zshrc`**

  Add these lines to your `~/.zshrc`:
  ```sh
  export TWEEPY_BEARER_TOKEN="<your_bearer_token>"
  export TWEEPY_CONSUMER_KEY="<your_consumer_key>"
  export TWEEPY_CONSUMER_SECRET="<your_consumer_secret>"
  export TWEEPY_ACCESS_TOKEN="<your_access_token>"
  export TWEEPY_ACCESS_TOKEN_SECRET="<your_access_token_secret>"
  ```
  Then reload your config:
  ```sh
  source ~/.zshrc
  ```

## Usage

Install from PyPI:

```sh
uv pip install twtr
```

Then tweet from the CLI:

```sh
twtr "your tweet here"
```

If you get an error about missing API keys, see the setup instructions above.

The script will use the environment variables from your `.env` file or shell config.