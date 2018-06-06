import os

USER_AGENT = os.getenv('USER_AGENT', '')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///database.sqlite')
