from sql_alchemy_db import db

class Climb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climb_name = db.Column(db.String(200))
    climb_type = db.Column(db.String(10))
    climb_grade = db.Column(db.String(4))
    climb_rating = db.Column(db.Integer(4))
    
#later additions:
#climb_description = db.Column(db.String(1000))
#done = db.Column(db.Boolean)