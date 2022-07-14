from app import db


class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    TeamName = db.Column(db.String(64), index=True, nullable=False)

class Events(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    EventName = db.Column(db.String(64), index=True, nullable=False)
    Sport = db.Column(db.String(64), index=True, nullable=False)
    NZTeam = db.Column(db.Integer, index=True, nullable=False)

class Members(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    TeamID = db.Column(db.Integer, db.ForeignKey('teams.id')) 
    Teams = db.relationship("Teams", backref=db.backref("teams", uselist=False))
    FirstName = db.Column(db.String(64), index=True, nullable=False) 
    LastName = db.Column(db.String(64), index=True, nullable=False)
    City = db.Column(db.String(64), index=True, nullable=False)
    Birthdate = db.Column(db.String(64), index=True, nullable=False)

class Event_Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    StageName = db.Column(db.String(64), index=True, nullable=False) 
    EventID = db.Column(db.Integer, db.ForeignKey('events.id')) 
    Events = db.relationship("Events", backref=db.backref("events", uselist=False))
    Location = db.Column(db.String(64), index=True, nullable=False) 
    StageDate = db.Column(db.String(64), index=True, nullable=False) 
    Qualifying = db.Column(db.Boolean, default=False, nullable=False)
    PointsToQualify = db.Column(db.Float, default=False, nullable=False)

# class Event_Stage_Results(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  
#     StageID = db.Column(db.Integer, db.ForeignKey('event_stage.id')) 
#     Event_Stage = db.relationship("Event_Stage", backref=db.backref("event_stage", uselist=False))
#     MemberID = db.Column(db.Integer, db.ForeignKey('members.id'))
#     Members = db.relationship("Members", backref=db.backref("members", uselist=False))
#     PointsScored = db.Column(db.Float, default=False, nullable=False)
#     Position = db.Column(db.Integer, index=True, nullable=False)
