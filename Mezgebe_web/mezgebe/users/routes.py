from flask import Blueprint
from mezgebe import app, db, bcrypt, mail
from mezgebe.models import User, Expense
from flask import render_template, flash, redirect, url_for, abort, request
from mezgebe.users.forms import UserRegisterationForm, UserLoginForm, PasswordResetForm, PasswordChangeForm
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    """ A Route To Handle a New User Registeration Process """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
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
        return redirect(url_for('users.login'))
    return render_template('registeration.html', title='Register', form=registeration_form)


@users.route('/Login', methods=['GET', 'POST'])
def login():
    """ A Route To Handle a User Login Process """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    login_form = UserLoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember_me.data)
            return redirect(url_for('main.home'))
        else:
            flash('Invalid credential. Please check email or password!')
    return render_template('login.html', form=login_form)


@users.route('/Logout')
def logout():
    """ A Route TO Handle a User Logout Process """
    logout_user()
    return redirect(url_for('users.login'))


@users.route('/account')
@login_required
def account():
    """ A Route To Handle a User Restriction """
    return render_template('account.html', title='Account')


def send_reset_email(user):
    """ A Function To Send a Password Reset
        Email For a User.

        - Flask_mail being used
    """
    token = (user.get_reset_token())
    reset_message = Message('Password Reset Request Instruction',
                            sender='danielshitaye10@gmail.com',
                            recipients=[user.email]
                            )
    reset_message.body = f'''Reset Your Password.
    {url_for('password_reset', token=token, _external=True)}
    click on the link attached.'''

    mail.send(reset_message.encode('utf-8'))



@users.route('/password_reset_request',  methods=['GET', 'POST'])
def password_reset():
    """ A Route To Handle a Password Reset Process """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    reset_form = PasswordResetForm()
    if reset_form.validate_on_submit():
        user = User.query.filter_by(email=reset_form.email.data).first()
        send_reset_email(user)
        flash('Password Reset Email has been sent. Please Check Your Email.', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_form.html', title='Password Reset', form=reset_form)



@users.route('/reset_password/<token>',  methods=['GET', 'POST'])
def password_change():
    """ A Route To Handle a Password Change Process """
    if current_user.is_authenicated:
        return redirect(url_for('main.home'))

    user = User.verify_token(token)
    if user is None:
        flash('Password Reset Token is Invalid Or Expired.', 'warning')
        return redirect(url_for('password_reset'))
    reset_form = PasswordChangeForm()
    if reset_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
                reset_form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Password has been changed successfull now you can login!', 'success')
        return redirect(url_for('users.login'))
    return render_template('password_change.html',
                               title='Password Change', form=reset_form)
