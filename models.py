from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    fixtures = db.relationship('User', 
    secondary="attended_games", backref="users")
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
        }

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    number = db.Column(db.Integer)
    age = db.Column(db.Integer)
    position = db.Column(db.String)
    nationality = db.Column(db.String)
    image = db.Column(db.String)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "number": self.number,
            "age": self.age,
            "position": self.position,
            "nationality": self.nationality,
            "image": self.image
        }

class Fixture(db.Model):
    __tablename__ = "fixtures"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    number = db.Column(db.Integer)
    # user = db.relationship('User', secondary="attended_games", backref="fixtures")
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Attended_Game(db.Model):
    __tablename__ = "attended_games"
    
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    fixture_id = db.Column(db.Integer, db.ForeignKey('fixtures.id'))
