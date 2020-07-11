from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
prefix = os.getenv('BOT_PREFIX')