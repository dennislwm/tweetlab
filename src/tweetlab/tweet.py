import tweepy

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                    M A I N   C L A S S                                   |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
class Pytweepy():

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                   C O N S T R U C T O R                                  |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def __init__(self, data):
    #----------------------------
    # initialize class _CONSTANTS
    self._init_meta()
    self.api = None

    #-------------
    # authenticate
    #   returns class tweepy.api.API
    #   irregardless of valid API keys
    auth = tweepy.OAuthHandler(
      data["twitter"]["api_key"],
      data["twitter"]["api_key_secret"]
    )
    auth.set_access_token(
      data["twitter"]["access_token"],
      data["twitter"]["access_token_secret"]
    ) 
    self.api = tweepy.API(auth)

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                C L A S S   R E Q U E S T S                               |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""

  def create_tweet(self, str_text):
    """Create and post a new tweet

    Parameters:
    str_text (str): The text of your tweet

    Returns:
    int: Status (tweet) id
    """
    self.api.update_status(str_text)

  def get_user_id(self, str_screen_name):
    """Get Twitter user id

    Parameters:
    str_screen_name (str): Twitter user handle (screen name)

    Returns:
    int, str: Twitter user id
    """
    obj_user = self.api.get_user(screen_name = str_screen_name)
    return obj_user.id, obj_user.id_str

  def get_user_timeline_items(self, str_user_id, int_items=1):
    """Get tweets of user

    Parameters:
    str_user_id (str): Twitter user id
    int_items (int): number of tweet items Default=1 (All=0)

    Returns:
    dictionary: dict(id, text)
    """
    timeline = tweepy.Cursor(self.api.user_timeline).items(int_items)
    return [dict(id=tweet.id, text=tweet.text) for tweet in timeline]

  def send_dm(self, data):
    """Send a direct message to recipient

    Parameters:
    data (ruamel.yaml.comments.CommentedMap): data consists of recipient information

    Returns:
    NA
    """
    recipient_id, recipient_id_str = self.get_user_id( data["recipient"]["handle"] )
    try:
      self.api.send_direct_message(
        recipient_id_str,
        data["recipient"]["body"]
      )
    except tweepy.TweepError as e:
      # TweepError object is a structure of type List[dict]
      print(f"Tweepy Error {e.args[0][0]['code']}: {e.args[0][0]['message']}")

  """--------+---------+---------+---------+---------+---------+---------+---------+---------|
  |                                C L A S S   M E T A D A T A                               |
  |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
  def _init_meta(self):
      """
      | _strMETACLASS, _strMETAVERSION, _strMETAFILE used to save() and load() members
      """
      self._strMETACLASS = str(self.__class__).split('.')[1][:-2]
      self._strMETAVERSION = "0.1"
      """
      | Filename "_Class_Version_"
      """
      self._strMETAFILE = "_" + self._strMETACLASS + "_" + self._strMETAVERSION + "_"
