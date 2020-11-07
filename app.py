from flask import Flask, jsonify, request, redirect, url_for, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_wtf import FlaskForm
from wtforms import SelectField
import pymysql
import secrets
from datetime import date


from flask_sqlalchemy import SQLAlchemy

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SECRET_KEY']='SuperSecretKey'
#app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///extsql.db"            
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class aggregate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(255))
    name = db.Column(db.String(255))
    clusterId = db.Column(db.Integer)


class aggregatecapacityhistoryyearview(db.Model):
    aggregateid = db.Column(db.Integer, primary_key=True)
    periodEndTime = db.Column(db.String(255))
    UsedSum = db.Column(db.BigInteger)

class Form(FlaskForm):
    sitename = SelectField('site_name', choices=[('2985','Des Moine'),('1','Lancaster')])
    aggrname = SelectField('aggr_name', choices=[])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/storage', methods=['GET', 'POST'])
def storage():
    form = Form()
    form.aggrname.choices = [(aggr.id, aggr.name) for aggr in aggregate.query.filter_by(clusterId='1').all()]
    
    if request.method == 'POST':
        aggr = aggregate.query.filter_by(id=form.aggrname.data).first()
        return '<h1>SiteName: {}, AggrName: {}</h1>'.format(form.sitename.data, aggr.name)

    return render_template('storage.html', form=form)

@app.route('/api/all/<clid>')
def all(clid):
    all = db.session.query().with_entities(aggregate.clusterId,aggregate.name,aggregatecapacityhistoryyearview.periodEndTime,aggregatecapacityhistoryyearview.UsedSum).join(aggregatecapacityhistoryyearview,aggregate.id==aggregatecapacityhistoryyearview.aggregateid)\
        .filter(aggregate.clusterId==clid).order_by(aggregate.clusterId.asc(),aggregate.name.asc(),aggregatecapacityhistoryyearview.periodEndTime.asc()).all() 
        # .filter(aggregatecapacityhistoryyearview.periodEndTime>date(2020,5,1),aggregatecapacityhistoryyearview.periodEndTime<date(2020,8,18))\
         
    aggrArray = []

    for aggregate.clusterId,aggregate.name,aggregatecapacityhistoryyearview.periodEndTime,aggregatecapacityhistoryyearview.UsedSum in all:
        aggrObj = {}
        aggrObj['Cluster_id'] = aggregate.clusterId
        aggrObj['aggr_name'] = aggregate.name
        aggrObj['date'] = aggregatecapacityhistoryyearview.periodEndTime
        aggrObj['Capacity'] = aggregatecapacityhistoryyearview.UsedSum
        aggrArray.append(aggrObj)

    return jsonify([aggrArray])
    


