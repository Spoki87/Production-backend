from app.errors.auth_errors import auth_error_handler


def error_handler(app):
    auth_error_handler(app)