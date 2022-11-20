from flask import Flask
from flask_restx import Api

from app.config import Config
from app.dao.model.author import Author
from app.dao.model.book import Book
from app.database import db

from app.views.authors import author_ns
from app.views.books import book_ns


def create_app(config: Config) -> Flask:
	application = Flask(__name__)
	application.config.from_object(config)
	application.app_context().push()

	return application


def configure_app(application: Flask):
	db.init_app(application)
	api = Api(application)
	api.add_namespace(book_ns)
	api.add_namespace(author_ns)


def load_data():
	# Создаём 2 книги в виде сущностей от класса модели
	b1 = Book(id=1, name="Harry Potter", year=2000)
	b2 = Book(id=2, name="Le Comte de Monte-Cristo", year=1844)

	# Создаём 2 автора в виде сущностей от класса модели
	a1 = Author(id=1, first_name="John", last_name="Routing")
	a2 = Author(id=2, first_name="Aleksandre", last_name="Dumas")

	# Создаём необходимые таблицы
	app.app_context().push()
	db.create_all()

	# При помощи открытия сессия сохраняем наши книги в базу
	with db.session.begin():
		db.session.add_all([b1, b2])
		db.session.add_all([a1, a2])


if __name__ == '__main__':
	app_config = Config()
	app = create_app(app_config)
	configure_app(app)
	load_data()
	app.run()
