from flask import current_app
from flask_jwt_extended import create_access_token

from app.exceptions import UserExistsError, InvalidCredentialsError
from app.models.app_user import User
from app.extensions import db

from app.schemas.auth import UserRegisterDTO, UserLoginDTO


class AuthService:
    @staticmethod
    def register_user(user_register_dto:UserRegisterDTO):
        if User.query.filter_by(email=user_register_dto.email).first():
            raise UserExistsError()

        user = User(**user_register_dto.model_dump(exclude={"password"}))
        user.set_password(user_register_dto.password)

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def login_user(user_login_dto:UserLoginDTO):
        user = User.query.filter_by(email=user_login_dto.email).first()
        if not user or not user.check_password(user_login_dto.password):
            raise InvalidCredentialsError()

        jwt_expires_delta = current_app.config["JWT_EXPIRATION_TIME"]
        access_token = create_access_token(identity=str(user.id), fresh=True, expires_delta=jwt_expires_delta)

        return access_token, user
