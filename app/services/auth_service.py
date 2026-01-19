from datetime import timedelta

from flask import current_app
from app.exceptions import UserExistsError, InvalidCredentialsError
from app.models.app_user import User
from app.extensions import db
from flask_jwt_extended import create_access_token, config


class AuthService:
    @staticmethod
    def register_user(first_name, last_name, email, password):
        if User.query.filter_by(email=email).first():
            raise UserExistsError("User already exists")

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            raise InvalidCredentialsError("Invalid credentials")
        jwt_expires_delta = current_app.config["JWT_EXPIRATION_TIME"]
        access_token = create_access_token(identity=user.id, fresh=True, expires_delta=jwt_expires_delta)
        return access_token, user
