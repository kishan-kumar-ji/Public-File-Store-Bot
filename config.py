import os

API_ID = int(os.environ.get("API_ID", '25269253'))
API_HASH = os.environ.get("API_HASH", 'a4f351103f9cb0eb6cfed99770f648ad')
BOT_TOKEN = os.environ.get("BOT_TOKEN", '6704331949:AAGpmMmvuXYsBijwSyGaNsrVa2F_1iu5J3M')
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", '-1002065381146')
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID",'6669835291'))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1002055148028')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "0").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
