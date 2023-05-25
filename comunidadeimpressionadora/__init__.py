from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

# No terminal digitar, para gerar um token desses
# python
# import secrets
# secrets.token_hex(16)
# exit
app.config['SECRET_KEY'] = '6f93a296d4b6f9a3777617f90c81be12'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

# Por ultimo pois precisa do app para ser criada
from comunidadeimpressionadora import routes
