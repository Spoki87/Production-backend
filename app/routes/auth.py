from flask import Blueprint
from flask import request
from app.utils.response import success_response, error_response
from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    try:
        user = AuthService.register_user(
            data.get("first_name"),
            data.get("last_name"),
            data.get("email"),
            data.get("password")
        )
    except ValueError as e:
        if str(e) == "User exists":
            return error_response("User exist", "Email already exists", 409)
        return error_response("Error", str(e), 400)

    return success_response(message="User created successfully", status=201)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    try:
        token, user = AuthService.login_user(
            data.get("email"),
            data.get("password")
        )
    except ValueError as e:
        if str(e) == "Invalid credentials":
            return error_response("Invalid credentials", "Bad email or password", 401)
        return error_response("Error", str(e), 400)

    return success_response({"access_token": token})
