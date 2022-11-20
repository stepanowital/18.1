from flask import request
from flask_restx import Resource, Namespace

from app.container import author_service
from app.dao.model.author import AuthorSchema

author_ns = Namespace('authors')

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)


@author_ns.route('/')
class AuthorsView(Resource):
	def get(self):
		all_authors = author_service.get_all()
		return authors_schema.dump(all_authors), 200

	def post(self):
		req_json = request.json
		author_service.create(req_json)

		return "", 201


@author_ns.route('/<int:uid>')
class AuthorView(Resource):
	def get(self, uid: int):
		try:
			author = author_service.get_one(uid)
			return author_schema.dump(author), 200
		except Exception as e:
			return str(e), 404

	def put(self, uid: int):
		req_json = request.json
		req_json["id"] = uid

		author_service.update(req_json)

		return "", 204

	def patch(self, uid: int):
		req_json = request.json
		req_json["id"] = uid

		author_service.update_partial(req_json)

		return "", 204

	def delete(self, uid: int):
		author_service.delete(uid)

		return "", 204
