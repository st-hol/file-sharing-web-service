from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(app)

    app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
    bootstrap = Bootstrap(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.user_loader(load_user)
    login_manager.login_view = 'main.login'

    from .views import main 
    app.register_blueprint(main)

    return app





