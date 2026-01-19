from app.models.app_user import User
from app.extensions import db
from flask_jwt_extended import create_access_token

class AuthService:
    @staticmethod
    def register_user(first_name, last_name, email, password):
        if User.query.filter_by(email=email).first():
            raise ValueError("User exists")

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
            raise ValueError("Invalid credentials")

        access_token = create_access_token(identity=user.id)
        return access_token, user
