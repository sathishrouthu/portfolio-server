from flask import Flask
from flask_cors import CORS  # Import CORS


def create_app():
    app = Flask(__name__)

    # Enable CORS for all domains (useful for development)
    CORS(app)

    # Register blueprints and routes
    from app.routes.mail_routes import mail_bp
    app.register_blueprint(mail_bp)

    return app
