from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager





app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9ec9f7e76250a1aff186a5d4acc1215c093586fd8d473eb475cf4c351fb9c8f'

# Setup the database``
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create DB Instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Import the routes
from flask_blog import routes