from flask import Blueprint, jsonify, request
from app.services.ml_service import MLService

prediction_bp = Blueprint('prediction', __name__)
ml_service = MLService()

@prediction_bp.route('/', methods=['POST'])
def predict():
    data = request.get_json()
    # Call ML service here
    prediction = ml_service.predict(data)
    # Ensure response matches frontend expectation
    # frontend expects: data.price
    return jsonify({"price": prediction["prediction"], "data": data})
