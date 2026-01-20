from app.exceptions import UserExistsError, InvalidCredentialsError
from app.utils.response import error_response


def auth_error_handler(app):
    @app.errorhandler(UserExistsError)
    def handle_user_exists_error(e):
        return error_response("User with this email already exists", 409)

    @app.errorhandler(InvalidCredentialsError)
    def handle_invalid_credentials_error(e):
        return error_response("Invalid credentials", 401)

    @app.errorhandler(Exception)
    def handle_general_error(e):
        return error_response(str(e), 500)
