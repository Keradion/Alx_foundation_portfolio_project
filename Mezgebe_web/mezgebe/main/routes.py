from flask import Blueprint, render_template 
from flask_login import current_user, login_required
from mezgebe.models import Expense
from mezgebe.models import User

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    """ A Route To Handle Home Page For a User """
    if current_user.is_authenticated:
        counter = 0
        expense = ''
        expenses = Expense.query.filter_by(user_id=current_user.id).all()
        if expenses:
            expense = 'exit'
        return render_template(
                'home.html', expense=expense, expenses=expenses, title='Home Page', counter=counter)
    else:
        return render_template('home_landing.html')
