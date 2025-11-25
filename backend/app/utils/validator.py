def validate_prediction_request(data):
    required_fields = ['pickup', 'drop', 'time']
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
    return True, None
