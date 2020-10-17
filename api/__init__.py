from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from api.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from api.main.routes import main
    from api.movies.routes import movies

    app.register_blueprint(main)
    app.register_blueprint(movies)

    return app
