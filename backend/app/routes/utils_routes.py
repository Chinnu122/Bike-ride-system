from flask import Blueprint, jsonify

utils_bp = Blueprint('utils', __name__)

@utils_bp.route('/weather', methods=['GET'])
def get_weather():
    return jsonify({"message": "Weather endpoint"})

@utils_bp.route('/traffic', methods=['GET'])
def get_traffic():
    return jsonify({"message": "Traffic endpoint"})
