import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app


def send_email(to_email, subject, body):
    try:
        # Create a MIME message
        msg = MIMEMultipart()
        msg["From"] = current_app.config["SMTP_FROM_MAIL"]
        msg["To"] = to_email
        msg["Subject"] = subject

        # Attach the HTML body to the email
        msg.attach(MIMEText(body, "html"))  # Send as HTML email

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(current_app.config["SMTP_SERVER"], current_app.config["SMTP_PORT"]) as server:
            server.starttls()  # Start TLS (secure connection)
            server.login(current_app.config["SMTP_USERNAME"], current_app.config["SMTP_PASSWORD"])
            server.send_message(msg)

        return True, "Mail sent successfully"
    except Exception as e:
        return False, str(e)
