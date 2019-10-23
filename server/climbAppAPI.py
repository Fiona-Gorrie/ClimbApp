from flask import Blueprint, jsonify, request
from sql_alchemy_db import db
from models import Climb

climbApp_api = Blueprint('climbApp_api', __name__)
 
@climbApp_api.route('/climbs', methods=['GET'])
def serve_all_climbs():
    climb_instances = db.session.query(Climb).all()
    climb_items = [{"id": climb.id, "climb name": climb.climbName, "climb type": climb.climbType, "climb grade": climb.climbGrade, 
    "climb rating": climb.climbRating} for climb in climb_instances]
    return jsonify({"climb": climb_items})

"""@climbApp_api.route('/todo', methods=['POST'])
def add_todo():
    new_todo = Todo()
    new_todo.item = request.json["item"]
    new_todo.done = False
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(success=True)

@climbApp_api.route('/todo', methods=['PATCH'])
def toggle_done():
    todo_id = request.json["id"]
    target_todo = db.session.query(Todo).filter_by(id=todo_id).first()
    target_todo.done = not target_todo.done
    db.session.add(target_todo)
    db.session.commit()
    return jsonify(success=True)"""