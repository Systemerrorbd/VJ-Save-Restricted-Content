import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7283204274:AAGWSKMOuB6BKPf3dx1LlzCdwKmGiyqAD3c")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29297709"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a643e14cad0a1e06a4c5c9969c188922")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6997532394"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://voicegv69:9mlB2SLfuItDJBYL@cluster0.hukaz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "newbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
