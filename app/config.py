import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    JWT_EXPIRATION_TIME = timedelta(seconds=int(os.getenv("JWT_EXPIRATION_TIME", "3600")))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
