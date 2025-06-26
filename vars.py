#🄶🄰🄱🅄
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21716342"))
API_HASH = environ.get("API_HASH", "9aab81717b40ade1d805023b707a7136")
BOT_TOKEN = environ.get("BOT_TOKEN", "8166167899:AAHM0yIDKd4ClqZLH-uQpgOCoW8A1jwO-Mc")
OWNER = int(environ.get("OWNER", "6936425004"))
CREDIT = "🇬 🇦 🇧 🇺 "
AUTH_USER = os.environ.get('AUTH_USERS', '6936425004').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
