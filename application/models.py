from application import db


class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clubname = db.Column(db.String(30), nullable=False)
    clublocation = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    clubmanager = db.Column(db.String(30), nullable=False)
    boxer = db.relationship('Boxer', backref='myclub', lazy=True) 


class Boxer(db.Model):
    clubid = db.relationship(Club)
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    weightclass = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    club = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
