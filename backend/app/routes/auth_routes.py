from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

auth_bp = Blueprint('auth', __name__)
user_service = UserService()

@auth_bp.route('/login', methods=['POST'])
def login():
    # Mock login
    data = request.get_json()
    if not data:
         return jsonify({"error": "No data provided"}), 400

    email = data.get('email')
    password = data.get('password')

    if user_service.authenticate(email, password):
        return jsonify({"message": "Login successful", "token": "mock-jwt-token"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    # Mock register
    data = request.get_json()
    return jsonify({"message": "User registered successfully"})
