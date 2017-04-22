from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    username = db.Column(db.String(30), index=True, nullable=False)

    def __init__(self, aFirstName, aLastName, aUsername):
        self.first_name = aFirstName
        self.last_name = aLastName
        self.username = aUsername

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(220), index=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, aMessage, aUserID):
        self.message = aMessage
        self.user_id = aUserID
        #self.messageAuthor = # get the user somehow.
