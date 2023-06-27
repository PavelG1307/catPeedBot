import constants
from pyrogram import Client, idle
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from logger import Logger

class Bot:
    def __init__(self, api_id, api_hash, bot_token, logger: Logger):
        self.bot: Client = Client(constants.BOT_NAME, api_hash=api_hash, api_id=api_id, bot_token=bot_token)
        self.timeout = 10
        self.is_connected = False
        self.logger = logger

    def add_btn_handler(self, handler):
        self.add_handler(CallbackQueryHandler(handler))

    def add_msg_handler(self, handler):
        self.add_handler(MessageHandler(handler))
    
    def add_handler(self, handler):
        self.bot.add_handler(handler)

    def start(self):
        self.bot.start()
        self.is_connected = True

    def idle(self):
        idle()

    def send_message(self, chat_id, text):
        self.bot.send_message(chat_id, text)
