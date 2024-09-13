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
        expenses = Expense.query.filter_by(user_id=current_user.id).all()
        return render_template('home.html', expenses=expenses, title='Home Page')
    else:
        return 'welcome'

