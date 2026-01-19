from flask import Blueprint, current_app
from flask import request

from app.utils.response import success_response
from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    AuthService.register_user(
        data.get("first_name"),
        data.get("last_name"),
        data.get("email"),
        data.get("password")
    )
    return success_response(message="User created successfully",status=201)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    token, user = AuthService.login_user(
        data.get("email"),
        data.get("password")
    )
    expires_in = int(current_app.config["JWT_EXPIRATION_TIME"].total_seconds())
    return success_response({"access_token": token,"expires_in":expires_in})
