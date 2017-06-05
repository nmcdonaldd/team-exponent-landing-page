from . import db
from datetime import datetime
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(60), index=True, nullable = False)
    password = db.Column(db.String(60), index=True, nullable = False)
    email = db.Column(db.String(60), index=True, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    email = db.Column(db.String(60), index=True, nullable=False)
    time = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    def __init__(self, first_name, email):
        self.first_name = first_name
        self.email = email

class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    def __init__(self):
        pass

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.String(34), nullable=False)
    name = db.Column(db.String(34), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def toDict(self):
        return {'device_id': self.UID, 'device_name': self.name, 'user_id': self.user_id}

    def __init__(self, UID, name, user):
        self.UID = UID
        self.name = name
        self.user_id = user
        pass

class force_reading(db.Model):
    __tablename__ = 'force'
    id = db.Column(db.Integer, primary_key=True)
    force_left = db.Column(db.Integer, index=True, nullable=True)
    force_middle = db.Column(db.Integer, index=True, nullable=True)
    force_right = db.Column(db.Integer, index=True, nullable=True)
    timestamp = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))

    def __init__(self, force_left, force_middle, force_right, device_id):
        self.force_left = force_left
        self.force_middle = force_middle
        self.force_right = force_right
        self.device_id = device_id

    def toDict(self):
        return {'id': self.id, 'force_left': self.force_left, 'force_middle': self.force_middle, 'force_right': self.force_right, 'timestamp': self.timestamp}

class temp_hum(db.Model):
    __tablename__ = 'temp_hum'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer, index=True, nullable=True)
    humidity = db.Column(db.Integer, index=True, nullable=True)
    timestamp = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))

    def __init__(self, temperature, humidity, device_id):
        self.temperature = temperature
        self.humidity = humidity
        self.device_id = device_id

    def toDict(self):
        return {'id': self.id, 'temperature': self.temperature, 'humidity': self.humidity, 'timestamp': self.timestamp}
