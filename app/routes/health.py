from flask import Blueprint, jsonify

# Define a blueprint for the health check route
health_bp = Blueprint('health', __name__)


@health_bp.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "up"}), 200
