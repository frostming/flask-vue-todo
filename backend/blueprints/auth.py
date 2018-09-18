from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import ValidationError, Length

from backend.models import User, db

bp = Blueprint('auth', __name__)


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Length(max=64)])
    password = PasswordField('Password', validators=[Length(8, 16)])
    confirm = PasswordField('Confirm Password')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).count() > 0:
            raise ValidationError('Username %s already exists!' % field.data)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Length(max=64)])
    password = PasswordField('Password', validators=[Length(8, 16)])
    remember = BooleanField('Remember Me')

    def validate_username(self, field):
        if not self.get_user():
            raise ValidationError('Invalid username!')

    def validate_password(self, field):
        if not self.get_user():
            return
        if not self.get_user().check_password(field.data):
            raise ValidationError('Incorrect password!')

    def get_user(self):
        return User.query.filter_by(username=self.username.data).first()


@bp.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    form = RegisterForm(data=user_data)
    if form.validate():
        user = User(username=user_data['username'], password=user_data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': form.errors}), 400


@bp.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    form = LoginForm(data=user_data)
    if form.validate():
        user = form.get_user()
        login_user(user, remember=form.remember.data)
        return jsonify({'status': 'success', 'user': user.to_json()})
    return jsonify({'status': 'error', 'message': form.errors}), 403


@bp.route('/session')
def get_session():
    if not current_user.is_authenticated:
        return jsonify({'status': 'error'}), 401
    return jsonify({'status': 'success', 'user': current_user.to_json()})


@bp.route('/logout')
def logout():
    logout_user()
    return jsonify({'status': 'success'})
