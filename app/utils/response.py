from flask import jsonify

def success_response(data=None, message="OK", status=200):
    resp = {"status": "success", "message": message}
    if data is not None:
        resp["data"] = data
    return jsonify(resp), status

def error_response(error, message=None, status=400):
    resp = {"status": "error", "error": error}
    if message:
        resp["message"] = message
    return jsonify(resp), status

__all__ = ["success_response", "error_response"]
