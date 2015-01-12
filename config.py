import os
from distutils.util import strtobool

class Config(object):
    DEBUG = strtobool(os.environ.get('DEBUG', 'false'))
    SECRET_KEY = os.environ.get('SECRET_KEY')