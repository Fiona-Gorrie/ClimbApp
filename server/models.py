from sql_alchemy_db import db

class Climbs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climbName = db.Column(db.String(200))
    climbType = db.Column(db.String(10))
    climbGrade = db.Column(db.String(4))
    climbRating = db.Column(db.Integer())
    
# class Type(db.Model):   
#     id = db.Column(db.Integer, primary_key=True)
#     gradeDifficulty = db.Column(db.String(10))

# class Grade(db.Model):   
#     id = db.Column(db.Integer, primary_key=True)
#     gradeDifficulty = db.Column(db.String(5))   

#later additions:
#user id and password
#add done = db.Column(db.Boolean) to climb for user to check
#climb_description = db.Column(db.String(1000))
