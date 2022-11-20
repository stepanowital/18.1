from marshmallow import Schema, fields

from app.database import db


class Book(db.Model):
	__tablename__ = 'book'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	year = db.Column(db.Integer)


class BookSchema(Schema):
	id = fields.Int()
	name = fields.Str()
	year = fields.Int()
	