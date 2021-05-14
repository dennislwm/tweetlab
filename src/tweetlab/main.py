import os

import config
from tweet import Pytweepy

def main():
  #----------------------------
  # create config if not exists
  new_file = 'tweetlab.yml'
  if not os.path.exists(new_file):
    new_file = input("Create a config file (leave empty for default): ") or new_file
    config.create_file(new_file)

  #------------
  # load config
  data = config.load_file(new_file)

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

if __name__ == "__main__":
  main()
