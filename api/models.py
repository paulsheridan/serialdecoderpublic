from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class ProductModel(db.Model):
    code = db.Column(db.String(1), primary_key=True)
    name = db.Column(db.String(20), unique=True)

class MonthBuilt(db.Model):
    code = db.Column(db.String(1), primary_key=True)
    name = db.Column(db.String(10), unique=True)

class ModelYear(db.Model):
    code = db.Column(db.String(1), primary_key=True)
    name = db.Column(db.String(10), unique=True)

class Factory(db.Model):
    code = db.Column(db.String(1), primary_key=True)
    name = db.Column(db.String(20), unique=True)
