from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

def menu():
  return render_template("menu.html")