

import os
import re
from dotenv import load_dotenv

load_dotenv()

class Config:
    ADMIN = os.environ.get("AUTH_USERS", "")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", ""))
    CHAT_ID = int(os.environ.get("CHAT_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SESSION_STRING = os.environ.get("SESSION_STRING", "")
