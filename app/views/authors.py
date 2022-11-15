from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import AuthorSchema, Author

author_ns = Namespace('authors')

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)


@author_ns.route('/')
class AuthorsView(Resource):
	def get(self):
		all_books = db.session.query(Author).all()
		return authors_schema.dump(all_books), 200

	def post(self):
		req_json = request.json
		new_book = Author(**req_json)

		with db.session.begin():
			db.session.add(new_book)

		return "", 201


@author_ns.route('/<int:uid>')
class AuthorView(Resource):
	def get(self, uid: int):
		try:
			book = db.session.query(Author).filter(Author.id == uid).one()
			return author_schema.dump(book), 200
		except Exception as e:
			return str(e), 404

	def put(self, uid: int):
		book = db.session.query(Author).get(uid)
		req_json = request.json

		book.first_name = req_json.get("first_name")
		book.last_name = req_json.get("last_name")

		db.session.add(book)
		db.session.commit()

		return "", 204

	def patch(self, uid: int):
		book = db.session.query(Author).get(uid)
		req_json = request.json

		if "first_name" in req_json:
			book.first_name = req_json.get("first_name")
		if "last_name" in req_json:
			book.last_name = req_json.get("last_name")

		db.session.add(book)
		db.session.commit()

		return "", 204

	def delete(self, uid: int):
		book = db.session.query(Author).get(uid)
		db.session.delete(book)
		db.session.commit()
		return "", 204
