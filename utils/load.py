import os
#from dotenv import load_dotenv

#load_dotenv()


def get_token():
	token = os.getenv('DISCORD_TOKEN')
	return token

def get_prefix():
	prefix = os.getenv('BOT_PREFIX')
	return prefix

def get_db():
	db  = os.getenv('database')
	return db