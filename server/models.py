from sql_alchemy_db import db

class Climb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climbName = db.Column(db.String(200))
    climbType = db.Column(db.String(10))
    climbGrade = db.Column(db.String(4))
    climbRating = db.Column(db.Integer())
    
#later additions:
#climb_description = db.Column(db.String(1000))
#done = db.Column(db.Boolean)