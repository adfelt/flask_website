import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail





app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9ec9f7e76250a1aff186a5d4acc1215c093586fd8d473eb475cf4c351fb9c8f'

# Setup the database``
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create DB Instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

# Import the routes
from flask_blog.users.routes import users
from flask_blog.posts.routes import posts
from flask_blog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

