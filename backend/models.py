from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_json(self):
        return {k: getattr(self, k) for k in ('id', 'text', 'done')}


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(200))
    todos = db.relationship('Todo', backref='user')

    def __init__(self, **kwargs):
        password = kwargs.pop('password')
        password = generate_password_hash(password)
        kwargs['password'] = password
        super(User, self).__init__(**kwargs)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_json(self):
        return {'id': self.id, 'username': self.username}
