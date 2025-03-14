from flask import Flask
from config import config
from app.blueprints.auth import auth_bp
from app.blueprints.index import index_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mongoengine

db = SQLAlchemy()
mongo = mongoengine

migrate = Migrate()

def createApp(configName='default'):
    """Application factory function"""
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config[configName])

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import sql_models

    mongo.connect(
        host=app.config['MONGO_URI']
    )

    # Initialize components
    # (This would be where you initialize database, cache, etc.)
    
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp)

    return app