from os import getenv

from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

db = PostgresqlDatabase(
	database=getenv('DB_DATABASE'),
	user=getenv('DB_USER'),
	password=getenv('DB_PASSWORD'),
	host=getenv('DB_HOST'),
	port=getenv('DB_PORT')
)

def get_db():
	return db
