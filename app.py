from flask import Flask, render_template, session, redirect, url_for, flash, request, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
import time, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'database.sqlite'
db = SQLAlchemy(app)

@app.route('/', methods=['GET','POST'])
def login():

    session['admin_id'] = user.admin_id
    session['name'] = user.admin_name



if __name__ == '__main__':
    app.run()
