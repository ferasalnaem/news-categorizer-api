from flask import Flask
from pymongo import MongoClient
from app.config import Config

mongo_client = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    global mongo_client
    mongo_client = MongoClient(app.config['MONGO_URI'])

    #Register routes
    from app.routes import init_routes
    init_routes(app)

    return app