from datetime import datetime
from mezgebe import db, login_manager, app
from flask_login import UserMixin
from uuid import uuid4
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


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

    def get_reset_token(self, duration_in_sec=1024):
        """ Return Password Reset Token """
        serializer = Serializer(app.config['SECRET_KEY'], duration_in_sec)
        return serializer.dumps({'user_id': (self.id)}).decode('utf-8')


    @staticmethod
    def verify_token(token):
        """ Verify Reset Token validity """
        serializer = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = serializer.loads(token)['user_id']
            return User.query.filter_by(id=user_id).first()
        except:
            return None


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

