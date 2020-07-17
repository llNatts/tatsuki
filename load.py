import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
prefix = os.getenv('BOT_PREFIX')