import os


class Config:
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp-relay.brevo.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    SMTP_FROM_MAIL = os.getenv("SMTP_FROM_MAIL")
