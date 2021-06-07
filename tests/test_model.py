import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from tweetlab import model
from tweetlab.model import insert_tweet, insert_deleted

@pytest.fixture(scope="session")
def engine():
  return create_engine("sqlite:///test.db", echo=True)

@pytest.fixture(scope="session")
def tables(engine):
  model.base.metadata.create_all(engine)
  yield
  model.base.metadata.drop_all(engine)

@pytest.fixture
def session(engine, tables):
  """
  Returns an sqlalchemy session, and 
  after that tears down everything properly.
  """
  connection = engine.connect()
  transaction = connection.begin()
  session = Session(bind=connection)
  yield session
  session.close()
  transaction.rollback()
  connection.close()

def test_tweets(session):
  result = insert_tweet(session, "1", "this is a tweet")
  for row in result:
    print(f"user_id: {row.user_id}")
    print(f"text: {row.text}")

def test_deleted(session):
  result = insert_deleted(session, "2", "this is a deleted tweet")
  for row in result:
    print(f"user_id: {row.user_id}")
    print(f"text: {row.text}")
