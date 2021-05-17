import os
import typer

app = typer.Typer()

import config
from tweet import Pytweepy

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                C O M M A N D   C R E A T E                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@app.command()
def create(conf_file: str = typer.Argument( 
  'tweetlab.yml',
  help="config file"
)):
  """
  Create config file
  """
  conf_file = input("Create a config file (leave empty for default): ") or conf_file
  if os.path.exists(conf_file):
    str_confirm = input(f"Do you want to overwrite {conf_file} (only 'yes' will be accepted)? ")
    if str_confirm.lower() == 'yes':
      config.create_file(conf_file)
    else:
      raise typer.Abort()

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                 C O M M A N D   T W E E T                                |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@app.command()
def tweet(conf_file: str = 'tweetlab.yml'):
  """
  Update status (tweet)
  """
  data = config.load_file(conf_file)

  #------------
  # auth client
  client = Pytweepy(data)

  #-------------
  # confirmation
  print( "tweet status:\n" )
  print( data["tweet"]["status"] )
  print( "\n" )
  str_confirm = input(f"Do you want to send this tweet (only 'yes' will be accepted)? ")
  if str_confirm.lower() == 'yes':
    #-----------------------
    # updates status (tweet)
    if data["tweet"]["status"]:
      client.create_tweet( data["tweet"]["status"] )
  else:
    raise typer.Abort()

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                  C O M M A N D   S E N D                                 |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@app.command()
def send(conf_file: str = 'tweetlab.yml'):
  """
  Send direct message
  """
  data = config.load_file(conf_file)

  #------------
  # auth client
  client = Pytweepy(data)

  #-------------
  # confirmation
  print( "recipient body:\n" )
  print( data["recipient"]["body"] )
  print( "\n" )
  str_confirm = input(f"Do you want to send this direct msg (only 'yes' will be accepted)? ")
  if str_confirm.lower() == 'yes':
    #---------
    # send msg
    if data["recipient"]["body"]:
      client.send_dm(data)
  else:
    raise typer.Abort()

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                C O M M A N D   D E L E T E                               |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
@app.command()
def delete(num: int = 1, conf_file: str = 'tweetlab.yml'):
  """
  Delete status (tweet)
  """
  if num > 5:
    typer.echo("NUM must be between 1 and 5")
    raise typer.Exit(code=1)
  data = config.load_file(conf_file)

  #------------
  # auth client
  client = Pytweepy(data)

  #------------
  # get user id
  int_id, str_id = client.get_user_id( data["tweet"]["handle"] )

  #-------------
  # confirmation
  dic_tweet = client.get_user_timeline_items(str_id, num)
  for tweet in dic_tweet:
    print(tweet)
  str_confirm = input(f"Do you want to delete the tweet(s) (only 'yes' will be accepted)? ")
  if str_confirm.lower() == 'yes':
    #----------------------
    # delete status (tweet)
    for tweet in dic_tweet:
      client.api.destroy_status(tweet['id'])
  else:
    raise typer.Abort()

if __name__ == "__main__":
  app()
