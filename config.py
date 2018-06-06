import os

REDDIT_API_ID = os.getenv('REDDIT_API_ID', '')
REDDIT_API_SECRET = os.getenv('REDDIT_API_SECRET', '')
USER_AGENT = os.getenv('USER_AGENT', '')
SUBREDDIT = os.getenv('SUBREDDIT', '/')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///database.sqlite')
