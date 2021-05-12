# tweetlab

Test driven development ["TDD"] of an tweet client.

<!-- TOC -->

- [tweetlab](#tweetlab)
  - [TL;DR](#tldr)
  - [Project](#project)
    - [Creating a config file](#creating-a-config-file)
    - [Creating a Twitter API](#creating-a-twitter-api)
  - [Usage](#usage)
    - [Installing on your workstation](#installing-on-your-workstation)
    - [Running the CLI](#running-the-cli)
  - [Project Structure](#project-structure)
  - [Test Driven Development](#test-driven-development)
    - [Creating a test config file](#creating-a-test-config-file)
    - [Running the tests](#running-the-tests)
  - [References](#references)
    - [Troubleshooting](#troubleshooting)

<!-- /TOC -->

## TL;DR

![Example Usage](demo.gif)

## Project

Create a CLI tool that we can use to easily send a tweet via `tweepy`. The CLI checks if the config file `tweetlab.yml` exists. Otherwise it will prompt the user to create a new config file, and asks the user for these required fields (unless specified otherwise):

1. twitter api_key
2. twitter api_key_secret
3. twitter bearer_token
4. twitter access_token
5. twitter access_token_secret
6. tweet handle
7. recipient handle
8. recipient body (type | for multi line)

### Creating a config file

If you plan to use the `tweet` module but not the CLI, you will have to manually create a config file. 

Touch a file `tweetlab.yml` in the root folder and copy and paste the following:

```yaml
twitter:
  api_key: "<your_twitter_api_key>"
  api_key_secret:  "<your_twitter_api_key_secret>"
  bearer_token: "<your_twitter_bearer_token>"
  access_token: "<your_twitter_access_token>"
  access_token_secret: "<your_twitter_access_token_secret>"
tweet:
  handle: "<your_twitter_handle>"
recipient:
  handle: "<recipient_twitter_handle>"
  body: "hello, world\n\n\
    \ Nice to meet you."
```

### Creating a Twitter API

First, login to your Twitter developer account. Go to the [Twitter Developer site](https://developer.twitter.com/en) to apply if you don't have one.

Twitter grants authentication credentials to apps, not accounts. To register your app, go to your [Twitter apps page](https://developer.twitter.com/en/apps) and select "Add App" option.

Don't select `V2 Access`, but `V1.1 Access` instead, as both the `access_token` and `access_token_secret` will not be given in the V2. The access token and secret represent the user identity, i.e. your Twitter user account.

If you are using Twitter for its general APIs, and not any private user APIs, then you only use the `bearer_token`. The `access_token` and `access_token_secret` are used in combination with `api_key` and `api_key_secret`.

Test Twitter API:

```bash
curl -X GET -H "Authorization: Bearer <BEARER TOKEN>" "https://api.twitter.com/2/tweets/20"
```

## Usage

### Installing on your workstation

Activate the pipenv environment by running `pipenv shell`. Then install the Python dependencies.

```bash
pipenv install
```

### Running the CLI

Ensure that you are in the `pipenv shell` environment first. To use the CLI tool.

```bash
python src/tweetlab/main.py
```

To use these modules within your Python script.

```python
from tweetlab import config
from tweetlab.tweet import Pytweepy
```

---
## Project Structure
     tweetlab/                        <-- Root of your project
       |- .gitignore                  <-- GitHub ignore 
       |- Makefile                    <-- Make file
       |- Pipfile                     <-- Pipenv 
       |- Pipfile.lock                <-- Pipenv lock 
       |- README.md                   <-- GitHub README markdown 
       +- src/
          +- tweetlab/                <-- Holds any business logic
             |- __init__.py
             |- config.py             <-- Python module to create or load config
             |- tweet.py              <-- Python module to compose tweet and interface with tweepy
             |- main.py               <-- Python module to demo the modules
       +- tests/                      <-- Holds any automated tests
          |- test_config.py           <-- Python script to test config.py
          |- test_tweet.py            <-- Python script to test tweet.py

---
## Test Driven Development

For this project, we're using `pytest` as our testing framework. We wrote a line in our `Makefile` that utilizes the `pytest`.

The file `test_config.py` ensures that our `config` module works as expected.

The file `test_tweet.py` ensures that our `tweet` module works as expected.

### Creating a test config file

In order to run the tests, you will have to create a test config file. 

Touch a file `test.yml` in the root folder and copy and paste the following:

```yaml
twitter:
  api_key: ""
  api_key_secret: ""
  bearer_token: ""
  access_token: ""
  access_token_secret: ""
tweet:
  handle: ""
recipient:
  handle: ""
  body: "hello, world\n\n\
    \ Nice to meet you."
```

### Running the tests

Ensure that you are in the pipenv environment by running `pipenv shell`. To run the test.

```bash
make
```

To run the test in verbose mode, use `make verbose` instead.

## References

* [How to Make a Twitter Bot in Python With Tweepy](https://realpython.com/twitter-bot-python-tweepy)

* [tweepy.API — Twitter API v1.1 Reference](https://docs.tweepy.org/en/latest/api.html)

* [API reference index | Twitter Developer](https://developer.twitter.com/en/docs/api-reference-index#twitter-api-v1)

### Troubleshooting

* [Support for Twitter API v2 · Issue #1472 · tweepy/tweepy](https://github.com/tweepy/tweepy/issues/1472)

* [how can I get authentication for the engagement endpoint using a bearer token](https://stackoverflow.com/questions/58943052/with-the-twitter-api-how-can-i-get-authentication-for-the-engagement-endpoint)
