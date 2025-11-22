def format_response(data, status=200, message="Success"):
    return {"status": status, "message": message, "data": data}
