from fastapi import FastAPI

from .routers import category
from .database import get_db

app = FastAPI()
db = get_db()

app.include_router(category.router)


@app.on_event('startup')
def startup():
	print('test')
	db.connect()


@app.on_event('shutdown')
def shutdown():
	if not db.is_closed():
		db.close()


@app.get('/')
async def root():
	return {'ping': 'pong'}
