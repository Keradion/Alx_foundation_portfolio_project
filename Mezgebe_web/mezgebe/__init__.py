from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '15acbc2e1b59e2e04cb76ed5a2c9b9f3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'danielshitaye10@gmail.com'
app.config['MAIL_PASSWORD'] =64406422
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

mail = Mail(app)

from mezgebe.main.routes import main
app.register_blueprint(main)

from mezgebe.users.routes import users
app.register_blueprint(users)

from mezgebe.expenses.routes import expenses
app.register_blueprint(expenses)
