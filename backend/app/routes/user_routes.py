from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
def get_profile():
    return jsonify({"message": "User profile endpoint"})

@user_bp.route('/history', methods=['GET'])
def get_history():
    return jsonify({"message": "User history endpoint"})
