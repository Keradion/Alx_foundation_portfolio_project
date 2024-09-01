from mezgebe import app
from flask import render_template, flash, redirect, url_for
from mezgebe.forms import UserRegisterationForm, UserLoginForm
from mezgebe.models import User, Expense, Category


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
    registeration_form = UserRegisterationForm()
    if registeration_form.validate_on_submit():
        flash('New User Account Created Successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('registeration.html', title='Register', form=registeration_form)


@app.route('/Login', methods=['GET', 'POST'])
def login():
    """ A Route To Handle a User Login Process """
    login_form = UserLoginForm()
    return render_template('Login.html', form=login_form)
