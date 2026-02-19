from flask import Flask

from app.extensions import db, jwt
from app.errors import error_handler
from app.routes.auth import auth_bp
from app.routes.products import products_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    jwt.init_app(app)
    error_handler(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(products_bp, url_prefix="/api")
#test
    return app
