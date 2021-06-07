from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

#
# initialize variables
# engine = db.create_engine("sqlite:///tweetlab.db")
base = declarative_base()
# session = orm.scoped_session(orm.sessionmaker())(bind=engine)
# base.metadata.bind = engine

#
# Replace flask_sqlalchemy with sqlalchemy
#   base == db.Model
#   session == db.session
#   other db.* values are in sa.*
#     old: db.Column(db.Integer,db.ForeignKey('s.id'))
#     new: sa.Column(sa.Integer,sa.ForeignKey('s.id'))
#   except relationship, and backref, those are in orm
#     orm.relationship, orm.backref
#   then to create the tables:
#     base.metadata.create_all()

class Tweets(base):
  __tablename__ = 'tweets'
  id            = db.Column(db.Integer, primary_key=True)
  user_id       = db.Column(db.String(20), nullable=False)
  text          = db.Column(db.String(280), nullable=False)

  def to_json(self):
    """
    Return the JSON serializable format
    """
    return {
      'id': self.id,
      'user_id': self.user_id,
      'text': self.text
    }

class Deleted(base):
  __tablename__ = 'deleted'
  id            = db.Column(db.Integer, primary_key=True)
  user_id       = db.Column(db.String(20), nullable=False)
  text          = db.Column(db.String(280), nullable=False)

  def to_json(self):
    """
    Return the JSON serializable format
    """
    return {
      'id': self.id,
      'user_id': self.user_id,
      'text': self.text
    }

def insert_tweet(session, str_user_id, str_text):
  assert(session)
  assert(str_user_id)
  assert(str_text)

  obj_tweet = Tweets(
    user_id = str_user_id, 
    text    = str_text
  )
  session.add(obj_tweet)
  session.commit()
  return session.query(Tweets).filter(Tweets.user_id==str_user_id).filter(Tweets.text==str_text)

def insert_deleted(session, str_user_id, str_text):
  assert(session)
  assert(str_user_id)
  assert(str_text)

  obj_tweet = Deleted(
    user_id = str_user_id, 
    text    = str_text
  )
  session.add(obj_tweet)
  session.commit()
  return session.query(Deleted).filter(Deleted.user_id==str_user_id).filter(Deleted.text==str_text)
