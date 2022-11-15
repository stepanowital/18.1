class Config:
	Debug = True
	SECRET = "Test"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	