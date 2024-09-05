from mezgebe import app, db, bcrypt
from mezgebe.models import User
from flask import render_template, flash, redirect, url_for
from mezgebe.forms import UserRegisterationForm, UserLoginForm
from mezgebe.models import User, Expense, Category
from flask_login import login_user, logout_user, current_user, login_required 



expenses = [ {'name' : 'daniel'} ]
@app.route('/')
@app.route('/home')
def home():
    """ A Route To Handle Home Page For a User """
    return render_template('home.html', expenses=expenses, title='Home Page')


@app.route('/about')
def about():
    """ A Route To Handle About Page """
    return render_template('about.html', title='About Page')


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

@app.route('/account')
@login_required
def account():
    """ A Route To Handle a User Restriction """
    return render_template('account.html', title='Account')
