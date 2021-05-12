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

  #-------------
  # confirmation
  str_confirm = input(f"Do you want to send this tweet (only 'yes' will be accepted)? ")
  if not str_confirm.lower() == 'yes':
    return

  #------------
  # auth client
  client = Pytweepy(data)

  #---------
  # send msg
  client.send_dm(data)

if __name__ == "__main__":
  main()
