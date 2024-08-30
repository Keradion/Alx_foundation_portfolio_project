from flask import Flask, render_template, flash, redirect, url_for
from forms import UserRegisterationForm, UserLoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '15acbc2e1b59e2e04cb76ed5a2c9b9f3'

expenses = [
        {
            'Date':'8/24/2024',
            'Amount': '2464',
            'Reason': 'Gym subscription',
            'Category': 'Entertainmnet'
        }
        ]


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


if __name__ == '__main__':
    app.run(debug=True)
