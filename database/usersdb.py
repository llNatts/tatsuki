from pymongo import MongoClient
from database import connection
import os
import json
from random import randint



def usersList():
	users = connection.connUserCl()
	lista = users.userscollection
	return lista

def usersReturnList(user):
	db = usersList()
	isreturned = db.find_one({"userId": user.id})

	return isreturned

def Insert(user):
	db = usersList()
	isregister= db.find_one({"userId": user.id})
	if not isregister:
		try:		
			avatar = db.insert_one({
			"user": user.id,
				"userProfile": {
				"level": 0,
				"xp": 0,
				"coins": 0,
				"tier": 3,
				"oldTier": None
				},
			"userInfo": {
				"respect": 0,
				"warnings": 0
				}
			})
			print(f'[LOG]: Foi criado um banco de dados para o usuário: {user.name}/ {user.id}')
		except Exception as error:
			print(f"[LOG]: Ocorreu um erro ao criar o bando de dados do {user.name} / {user.id}")
	else:
		print(f'[LOG]: O usuário {user.name} / {user.id} já possui um banco de dados salvo')

def xpUpdate(user):
	xp = randint(1,10)
	json = usersList()
	try:
		istrue = json.find_one_and_update(
			{"user" : user.id},
			 { '$inc' :{"userProfile.xp": xp} }
			 )
		if not istrue:
			Insert(user)
	except Exception as error:
		print(error)