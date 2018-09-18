import os
from werkzeug.exceptions import HTTPException
from flask import Flask, jsonify, render_template
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager

from backend.models import db, User
from backend.blueprints import todos, auth

FRONTEND_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend')


def create_app():
    app = Flask(
        __name__, static_folder=os.path.join(FRONTEND_FOLDER, 'dist'),
        template_folder=FRONTEND_FOLDER
    )
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    CSRFProtect(app)
    Migrate(app, db)
    CORS(app)
    lm = LoginManager(app)

    @lm.user_loader
    def load_user(uid):
        return User.query.get(uid)

    @app.route('/')
    def index():
        return render_template('index.html')

    app.register_blueprint(todos.bp, url_prefix="/")
    app.register_blueprint(auth.bp, url_prefix="/auth")
    register_error_handlers(app)
    return app


def register_error_handlers(app):

    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return jsonify({'status': 'error', 'description': exc.description}), exc.code
