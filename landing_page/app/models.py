from . import db
from datetime import datetime
from sqlalchemy.sql import func

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    email = db.Column(db.String(60), index=True, nullable=False)
    time = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=str(datetime.now().strftime("%m/%d/%Y %H:%M")))

    def __init__(self, first_name, email):
        self.first_name = first_name
        self.email = email

class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=str(datetime.now().strftime("%m/%d/%Y %H:%M")))

    def __init__(self):
        pass

class temp_hum(db.Model):
    __tablename__ = 'temp_hum'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer, index=True, nullable=True)
    humidity = db.Column(db.Integer, index=True, nullable=True)
    timestamp = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=str(datetime.now().strftime("%m/%d/%Y %H:%M")))

    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

    def toDict(self):
        return {'id': self.id, 'temperature': self.temperature, 'humidity': self.humidity, 'timestamp': self.timestamp}
