from flask import Flask

from app.routes.health import health_bp
from app.routes.mail_routes import mail_bp
from app.routes.todo_routes import todo_bp

from app.extensions import db

from flask_cors import CORS  # Import CORS


def create_app():
    app = Flask(__name__)

    # Enable CORS for all domains (useful for development)
    CORS(app)

    # Configurations
    app.config.from_object('app.config.Config')

    # Initialize the database connection
    db.init_app(app)

    # Register Blueprints (Routes)
    app.register_blueprint(mail_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(todo_bp)

    return app
