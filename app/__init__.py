from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import HTTPException

db = SQLAlchemy()
jwt = JWTManager()


def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        response = e.get_response()
        response.data = jsonify({
            "status": "error",
            "error": e.name,
            "message": e.description,
            "code": e.code
        }).data
        response.content_type = "application/json"
        return response

    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({
            "status": "error",
            "error": "Internal Server Error",
            "message": "Something went wrong"
        }), 500


def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    register_error_handlers(app)

    return app
