from flask import Flask, request, Blueprint
from .controller import datas
from .extension import db
import os
from .model import Data

def create_app():
    app = Flask(__name__)
    app.secret_key = "Secret Key"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/crud'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("created")
    app.register_blueprint(datas)

    return app
