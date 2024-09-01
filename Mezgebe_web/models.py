class User(db.Model):
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
        return f'User('{self.first_name}', '{self.last_name}', '{self.user_name}')'

class Expense(db.Model):
    """
       Define Attributes for Expense Class
    """
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.String(1024), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.relationship('Category', ForeignKey('category.id', nullable=False)

    def __repr__(self):
        """
          Custom output for class Expense
        """
        return f'Expense('{self.description}', '{self.date}', '{self.amount}')'


class Category(db.Model):
    """
       Define Attributes for Category Class
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    category_expenses = db.relationship('Expense', backref='category')

    def __repr__(self):
        """
          Custom output for class Category
        """
        return f'Category('{self.name}')'
