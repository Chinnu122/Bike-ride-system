from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.database.db import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)
    db.init_app(app)

    # Register Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.prediction_routes import prediction_bp
    from app.routes.user_routes import user_bp
    from app.routes.utils_routes import utils_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(prediction_bp, url_prefix='/api/predict')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(utils_bp, url_prefix='/api/utils')

    return app
