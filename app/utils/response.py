from flask import jsonify

def success_response(data=None, message="OK", status=200):
    resp = {"status": "success", "message": message, "data": data}
    return jsonify(resp), status

def error_response(message=None, status=400):
    resp = {"status": "error", "message": message}
    return jsonify(resp), status