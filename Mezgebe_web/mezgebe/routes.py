from mezgebe import app, db, bcrypt
from mezgebe.models import User
from flask import render_template, flash, redirect, url_for
from mezgebe.forms import UserRegisterationForm, UserLoginForm, NewExpenseForm
from mezgebe.models import User, Expense
from flask_login import login_user, logout_user, current_user, login_required 



@app.route('/')
@app.route('/home')
@login_required
def home():
    """ A Route To Handle Home Page For a User """
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', expenses=expenses, title='Home Page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ A Route To Handle a New User Registeration Process """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    registeration_form = UserRegisterationForm()
    if registeration_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(registeration_form.password.data).decode('utf-8')
        new_user = User(user_name=registeration_form.user_name.data, 
                        first_name=registeration_form.first_name.data,
                        last_name=registeration_form.last_name.data,
                        email=registeration_form.email.data,
                        password=hashed_password
                        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account has been created and you can now login!', 'success')
        return redirect(url_for('login'))
    return render_template('registeration.html', title='Register', form=registeration_form)


@app.route('/Login', methods=['GET', 'POST'])
def login():
    """ A Route To Handle a User Login Process """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    login_form = UserLoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember_me.data)
            return redirect(url_for('home'))
        else:
            flash('Invalid credential. Please check email or password!')
    return render_template('login.html', form=login_form)




@app.route('/Logout')
def logout():
    """ A Route TO Handle a User Logout Process """
    logout_user()
    return redirect(url_for('home'))


@app.route('/expense/new_expense',  methods=['GET', 'POST'])
@login_required
def add_expense():
    """ A Route To Handle a Process To Create a New Expense By a User """
    new_expense_form = NewExpenseForm()
    if new_expense_form.validate_on_submit():
        new_expense = Expense(amount=new_expense_form.amount.data,
                              description=new_expense_form.description.data,
                              user_id=current_user.id)
        db.session.add(new_expense)
        db.session.commit()
        flash('New Expense Added Successfully', 'success')
        return redirect(url_for('home'))
    return render_template('expenseform.html', form=new_expense_form)


@app.route('/account')
@login_required
def account():
    """ A Route To Handle a User Restriction """
    return render_template('account.html', title='Account')
