import os.path
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SECRET_KEY = '789+%$2'
SQLALCHEMY_TRACK_MODIFICATIONS = True



