import os

here = os.path.dirname(__file__)

SECRET_KEY = 'flask-vue-todo-app'
WTF_CSRF_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

if 'DATABASE_URL' in os.environ:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(here, 'db.sqlite3')
