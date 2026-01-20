from flask import Blueprint, current_app
from flask import request

from app.schemas.auth import UserRegisterDTO, UserLoginDTO
from app.utils.response import success_response
from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    user_register_dto = UserRegisterDTO(**request.json)
    user = AuthService.register_user(user_register_dto)
    return success_response(data=user.to_dict(),message="User created successfully",status=201)

@auth_bp.route("/login", methods=["POST"])
def login():
    user_login_dto = UserLoginDTO(**request.json)
    token, user = AuthService.login_user(user_login_dto)
    expires_in = int(current_app.config["JWT_EXPIRATION_TIME"].total_seconds())
    return success_response({"access_token": token,"expires_in":expires_in})
