from flask import Flask
from app.routes.mail_routes import mail_bp
from flask_cors import CORS  # Import CORS


def create_app():
    app = Flask(__name__)

    # Enable CORS for all domains (useful for development)
    CORS(app)

    # Configurations
    app.config.from_object('app.config.Config')

    # Register Blueprints (Routes)
    app.register_blueprint(mail_bp)

    return app
