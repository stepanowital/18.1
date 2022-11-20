from app.dao.model.book import Book


# CRUD
class BookDAO:
	def __init__(self, session):
		self.session = session

	def get_one(self, bid):
		return self.session.query(Book).get(bid)

	def get_all(self):
		return self.session.query(Book).all()

	def create(self, data):
		book = Book(**data)

		self.session.add(book)
		self.session.commit()

		return book


	def update(self, book):
		self.session.add(book)
		self.session.commit()

		return book

	def delete(self, bid):
		book = self.get_one(bid)

		self.session.delete(book)
		self.session.commit()
