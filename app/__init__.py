from datetime import timedelta

from flask import Flask
from flask_cors import CORS

from app.config import Config
from app.extensions import db, migrate, bcrypt, jwt
from app.routes import register_routes


def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    app.config["JWT_TOKEN_EXPIRES"] = timedelta(minutes=30)
    app.config["JWT_REFRESH_EXPIRES"] = timedelta(days=30)

    jwt.init_app(app)


    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


    try:
        register_routes(app)
    except ImportError:
        pass

    return app
