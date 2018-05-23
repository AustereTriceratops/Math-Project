import os


class Config:
    # flask config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'

