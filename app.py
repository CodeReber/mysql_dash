from flask import Flask, jsonify, request, redirect, url_for, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pymysql
import secrets

from flask_sqlalchemy import SQLAlchemy

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SECRET_KEY']='SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1trtAll46@localhost/ocum_report'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


@app.route('/')
def index():
    return render_template('index.html')

