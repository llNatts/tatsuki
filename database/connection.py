from pymongo import MongoClient
from utils import load

def connUserCl():
	db = load.get_db()
	print(db)
	try:	
		client = MongoClient(db)
		db = client.tatsukidb
		return db
	except Exception as error:
		print(error)
		return error