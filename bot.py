# Don't Remove Credit Tg - @SystemErrorBD
# Subscribe YouTube Channel For Amazing Bot https://T.me/SystemErrorBF
# Ask Doubt on telegram @MR_ERR0RR

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
            "techvj login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ"),
            workers=50,
            sleep_threshold=10
        )

      
    async def start(self):
            
        await super().start()
        print('Bot Started Powered By @SystemErrorBD')

    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

Bot().run()
