from pymongo import MongoClient
from database import connection
import os
import json
from random import randint



def reactionList():
	reactionRole = connection.connUserCl()
	lista = reactionRole.reactionList
	return lista

def consult(messageid,channelid):
	db = reactionList()
	isreturned = db.find_one({"messageId": messageid, "channelId": channelid})
	return isreturned

def Insert(json):
	db = reactionList()
	isregister= consult(json['messageId'], json['channelId'])
	if not isregister:
		try:		
			db.insert_one(json)
			print(f'[LOG]: reaction role adicionado ')
		except Exception as error:
			print(f"[LOG]: Ocorreu um erro ao criar o bando de dados do reactionRole {error}")
	else:
		print(f'[LOG]:  O reaction role já existe')