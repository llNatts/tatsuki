from pymongo import MongoClient
from database import connection


def usersList():
	users = connection.connUserCl()
	lista = users.userscollection
	return lista

def usersReturnList(user):
	db = usersList()
	isreturned = db.find_one({"userId": user.id})
	print(isreturned)
	return isreturned

def Insert(user):
	db = usersList()
	isregister= db.find_one({"userId": user.id})
	if isregister == None:
		avatar = db.insert_one({
			"userId": user.id,
			"coins": 0,
			"level": 0,
			})
		print(f'[LOG]: Foi criado um banco de dados para o usuário: {user.name}/ {user.id}')