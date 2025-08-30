from flask import Flask
from app.routes.mail_routes import mail_bp

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config.from_object('app.config.Config')

    # Register Blueprints (Routes)
    app.register_blueprint(mail_bp)

    return app
