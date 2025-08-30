from flask import Blueprint, request, jsonify
from app.utils.email_utils import send_email

mail_bp = Blueprint('mail', __name__)


@mail_bp.route("/api/mail/send", methods=["POST"])
def send_mail():
    data = request.get_json()

    to_email = data.get("to")
    subject = data.get("subject")
    body = data.get("body")

    if not to_email or not subject or not body:
        return jsonify({"error": "Missing required fields"}), 400

    success, message = send_email(to_email, subject, body)

    if success:
        return jsonify({"success": True, "message": message})
    else:
        return jsonify({"success": False, "error": message}), 500
