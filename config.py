import os

class Config:
    SECRET_KEY = 'f8735405dc4f9dbfe576a407424561bb5dfb48b6bb4ee33fdb681537651ece36'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cars.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/uploads'