import os


class Config:
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp-relay.brevo.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    SMTP_FROM_MAIL = os.getenv("SMTP_FROM_MAIL")

    # Fetch MySQL configuration directly from environment variables
    MYSQL_USER = os.getenv('MYSQL_USER')  # Your MySQL username
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')  # Your MySQL password
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')  # Default to localhost if not set
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'sathish')  # Your MySQL database name

    # Build the MySQL connection URI for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
    print(SQLALCHEMY_DATABASE_URI)
    # SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable Flask-SQLAlchemy modification tracking

