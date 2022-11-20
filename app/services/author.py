from app.dao.author import AuthorDAO


class AuthorService:
	def __init__(self, dao: AuthorDAO):
		self.dao = dao

	def get_one(self, aid):
		return self.dao.get_one(aid)

	def get_all(self):
		return self.dao.get_all()

	def create(self, data):
		return self.dao.create(data)

	def update(self, data):
		aid = data.get('id')
		author = self.get_one(aid)

		author.first_name = data.get("first_name")
		author.last_name = data.get("last_name")

		self.dao.update(author)

	def update_partial(self, data):
		aid = data.get('aid')
		author = self.get_one(aid)

		if "first_name" in data:
			author.first_name = data.get("first_name")
		if "last_name" in data:
			author.last_name = data.get("last_name")

		self.dao.update(author)

	def delete(self, aid):
		self.dao.delete(aid)
