import os
from flask import Flask, render_template, jsonify, request
from sql_alchemy_db import db

def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///climbApp.db"
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    #app.register_blueprint(todos_api)

    return app

