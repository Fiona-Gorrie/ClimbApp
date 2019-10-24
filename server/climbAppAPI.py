from flask import Blueprint, jsonify, request
from sql_alchemy_db import db
from models import Climbs

climbApp_api = Blueprint('climbApp_api', __name__)
 
@climbApp_api.route('/climbs', methods=['GET'])
def serve_all_climbs():
    climb_instances = db.session.query(Climb).all()
    climb_items = [{"id": climb.id, "climb name": climb.climbName, "climb type": climb.climbType, "climb grade": climb.climbGrade, 
    "climb rating": climb.climbRating} for climb in climb_instances]
    return jsonify({"climb": climb_items})

@climbApp_api.route('/climbData', methods=['POST'])
def return_climb_data():
    climb_type = request.json["selected_climb_type"]
    climb_grade = request.json["selected_climb_grade"]
    return jsonify(climb_type=climb_type, climb_grade=climb_grade)

@climbApp_api.route('/climbResult', methods=['GET'])
def find_climb():
    climb_data = Climbs.query.all()
    print(climb_data)
    #matching_climb = [climb.climb_name for climb in climb_data]
    climb_array = [climb.climb_name for climb in climb_data]
    return jsonify(climb_array = climb_array)