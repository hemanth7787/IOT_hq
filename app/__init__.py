from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.login import LoginManager
from config import basedir

app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)

db = SQLAlchemy(app)



from app import views, models
