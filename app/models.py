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


class Author(db.Model):
	__tablename__ = 'author'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(100), nullable=False)
	last_name = db.Column(db.String(100), nullable=False)


class AuthorSchema(Schema):
	id = fields.Int()
	first_name = fields.Str()
	last_name = fields.Str()