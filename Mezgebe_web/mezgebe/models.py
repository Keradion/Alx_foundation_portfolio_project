from datetime import datetime
from mezgebe import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user

class User(db.Model, UserMixin):
    """
        Define Attributes for User Class
    """
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(10), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    expenses = db.relationship('Expense', backref='user')

    def __repr__(self):
        """
          Custom output for class User
        """
        return f"User('{self.first_name}', '{self.last_name}', '{self.user_name}')"

class Expense(db.Model):
    """
       Define Attributes for Expense Class
    """
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.String(1024), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        """
          Custom output for class Expense
        """
        return f"Expense('{self.description}', '{self.date}', '{self.amount}')"

