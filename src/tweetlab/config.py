from getpass import getpass
from ruamel.yaml import YAML

def load_file(filename):
  yaml = YAML()
  #---------------
  # Read from file
  with open(filename, 'r') as file:
    yml_return = yaml.load(file)
  return yml_return

def input_multi_line_str(prompt):
  lines = []
  line = input(prompt)
  if line == "|":
    while True:
      line = input("  Line " + str(len(lines)+1) + " (leave empty to end): " )
      if not line: 
        break
      lines.append(line)
    ret_str = '\n'.join(lines)
  else:
    ret_str = line
  return ret_str

def create_file(filename):
  yaml = YAML()
  init = ("""
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
      body: ""
  """)
  data = yaml.load(init)

  data["twitter"]["api_key"]              = getpass("Enter twitter API key (required): ")
  data["twitter"]["api_key_secret"]       = getpass("Enter twitter API secret key (required): ")
  data["twitter"]["bearer_token"]         = getpass("Enter twitter bearer token (required): ")
  data["twitter"]["access_token"]         = getpass("Enter twitter access token (required): ")
  data["twitter"]["access_token_secret"]  = getpass("Enter twitter access secret token (required): ")
  data["tweet"]["handle"]                 = input("Enter tweet handle (required): ")
  data["recipient"]["handle"]             = input("Enter recipient handle (required): ")
  data["recipient"]["body"]               = input_multi_line_str("Enter tweet body (required type '|' for multi line): ")

  with open(filename, 'w') as file:
    yaml.dump(data, file)
