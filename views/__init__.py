from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../db.sqlite')

db = SQLAlchemy(app)
from src.views.property_view import property_bp
app.register_blueprint(property_bp)
from src.views.user_view import users_bp
app.register_blueprint(users_bp)

@app.before_first_request
def create_table():
    db.create_all()
