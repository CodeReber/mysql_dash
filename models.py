from app import app

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class aggregate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(255))
    name = db.Column(db.String(255))

class aggregatecapacityhistoryyearview(db.Model):
    aggregateid = db.Column(db.Integer, primary_key=True)
    periodEndTime = db.Column(db.String(255))
    UsedSum = db.Column(db.BigInteger)


def get_all():
    all = aggregate.query.all()
    for a in all:
        print({a.name},{a.id})

def get_all_aggr_cap():
    all = aggregatecapacityhistoryyearview.query.all()
    for a in all:
        print({a.aggregateid},{a.periodEndTime},{a.UsedSum})

