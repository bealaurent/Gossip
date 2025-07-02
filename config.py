import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
DEFAULT_CHANNEL = int(os.getenv("DEFAULT_CHANNEL", 0))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()