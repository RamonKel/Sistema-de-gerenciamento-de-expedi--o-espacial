from app import app
from flask import Flask, render_template, request, flash, redirect, url_for
from database import db
from flask_migrate import Migrate

app = Flask(__name__)

db.init_app(app)
connect = "sqlite://bdexpedição.sqlite"

app.config['SECRET_KEY'] = 'AeroSpace01'
app.config['SQLALCHEMY_DATABASE_URI'] = connect
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

migrate = Migrate(app, db)

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

def menu():
  return render_template("menu.html")