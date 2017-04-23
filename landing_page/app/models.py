from app import db
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
