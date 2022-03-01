import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# import os

app = Flask(__name__)




# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY


app.config['SECRET_KEY'] = '5468e77745e8b9a5b55adbf16e9bdb9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #setting relative path for sqlite DB


db = SQLAlchemy(app) #creating an instance for DB
bcrypt = Bcrypt() # instantiating Bcrypt
login = LoginManager() #instantiating LoginManager

from blog import routes #imports route channel