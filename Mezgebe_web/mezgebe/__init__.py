from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from mezgebe.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
mail = Mail()


def create_app(config_class=Config):
    """
       Application Factory 
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    bcrypt.init_app(app)        
    login_manager.init_app(app)
    mail.init_app(app)

    from mezgebe.main.routes import main
    from mezgebe.users.routes import users
    from mezgebe.expenses.routes import expenses

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(expenses)

    return app
