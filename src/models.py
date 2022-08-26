from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    date_birth = db.Column(db.Date)

    def __init__(self, first_name, last_name, date_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth

    def __repr__(self):
        return f'<User: {self.first_name}>'

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(250))
    type = db.Column(db.String(50))
    city = db.Column(db.String(80))
    rooms = db.Column(db.Integer)
    char_rooms = db.Column(db.String(300))
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, name, description, type, city, rooms, char_rooms, owner_id):
        self.name = name
        self.description = description
        self.type = type
        self.city = city
        self.rooms = rooms
        self.char_rooms = char_rooms
        self.owner_id = owner_id

    def __repr__(self):
        return f'<Property: {self.name}>'



