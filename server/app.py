import os
from flask import Flask, render_template, jsonify, request
from sql_alchemy_db import db
from climbAppAPI import climbApp_api
import pandas as pd
#from sqlalchemy import create_engine

project_dir = os.path.dirname(os.path.abspath(__file__))
project_paths = project_dir.split("/")
project_paths.pop()
project_paths.append('db')
project_dir = "/".join(project_paths)

def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "climbApp.db"))
    app.config['SQLALCHEMY_ECHO'] = True
    #echo's the commands being generated by sqlalchemy, also helpful for debugging
    db.init_app(app)
    app.register_blueprint(climbApp_api)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all() 

def seed_db(app):
    df = pd.read_csv("climbs.csv")
    with app.app_context():
        df.to_sql(name='climbs', con=db.engine, index_label='id', if_exists='replace')


