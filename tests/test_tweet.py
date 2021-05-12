import os
import pytest
import requests
import tweepy

from tweetlab import config
from tweetlab.tweet import Pytweepy

test_file = "test.yml"

@pytest.fixture
def data():
  #----------------------------
  # create config if not exists
  new_file = test_file
  if not os.path.exists(new_file):
    new_file = input("Create a config file (leave empty for default): ") or new_file
    config.create_file(new_file)
  #------------
  # load config
  return config.load_file(new_file)

@pytest.fixture
def client(data):
  #---------------------
  # authenticate Twitter
  return Pytweepy(data)

def test_validate_tweepy_class(client):
  print( type(client.api) )
  assert type(client.api).__name__ == "API"

def test_validate_twitter_bearer_token(client):
  #--------------
  # JSON response
  #   Doc: https://developer.twitter.com/en/docs/twitter-api/v1/developer-utilities/configuration/api-reference/get-help-configuration
  assert "dm_text_character_limit" in client.api.configuration()

def test_validate_twitter_access_token(client, data):
  assert "screen_name", data["tweet"]["handle"] in client.api.get_settings()

def test_get_user_id(client, data):
  int_id, str_id = client.get_user_id( data["tweet"]["handle"] ) 
  assert int_id > 0
  assert int_id == int(str_id)
