from marshmallow import Schema, fields

from app.database import db


class Author(db.Model):
	__tablename__ = 'author'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(100), nullable=False)
	last_name = db.Column(db.String(100), nullable=False)


class AuthorSchema(Schema):
	id = fields.Int()
	first_name = fields.Str()
	last_name = fields.Str()