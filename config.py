import os

# Flask
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
DEBUG = os.environ.get('DEBUG', False)

# Telegram
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"
APP_URL = os.environ.get("APP_URL")
WEB_APP_URL = f"{APP_URL}/webapp"

# News API
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
