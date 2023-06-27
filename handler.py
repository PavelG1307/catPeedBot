import constants
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, ReplyKeyboardRemove
from datetime import datetime
from logger import Logger

class CustomHandler:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.lastPipi: datetime = None
        self.lastKaka: datetime = None

    def getMsgHandler(self, app):
        def handle(app: Client, msg: Message):
            try:
                if msg.text == '/start':
                    pipiBtn = KeyboardButton(constants.PIPI_BTN_TEXT)
                    kakaBtn = KeyboardButton(constants.KAKA_BTN_TEXT)
                    checkBtn = KeyboardButton(constants.CHECK_BTN_TEXT)
                    keyboard = ReplyKeyboardMarkup([[pipiBtn,kakaBtn], [checkBtn]])
                    msg.reply(constants.START_MESSAGE, reply_markup=keyboard)
                    return
                
                if msg.text == constants.KAKA_BTN_TEXT:
                    if self.lastKaka is None:
                        self.lastKaka = datetime.now()
                        msg.reply(constants.FIRST_TIME)
                        return
                    now = datetime.now()
                    diff = now - self.lastKaka
                    self.lastKaka = now
                    countHrs = round(diff.seconds / 3600, 2)
                    message = f'Кошке потребовалось {countHrs} часов чтобы сделать это!'
                    msg.reply(message)
                    return
                
                if msg.text == constants.PIPI_BTN_TEXT:
                    if self.lastPipi is None:
                        self.lastPipi = datetime.now()
                        msg.reply(constants.FIRST_TIME)
                        return
                    now = datetime.now()
                    diff = now - self.lastPipi
                    self.lastPipi = now
                    countHrs = round(diff.seconds / 3600, 2)
                    message = f'Кошке потребовалось {countHrs} часов чтобы сделать это!'
                    msg.reply(message)
                    return
                
                if msg.text == constants.CHECK_BTN_TEXT:
                    now = datetime.now()
                    diffPipi = '∞'
                    diffKaka = '∞'
                    if not self.lastPipi is None:
                        diffPipi = round((now - self.lastPipi).seconds / 3600, 2)
                    if not self.lastKaka is None:
                        diffKaka = round((now - self.lastKaka).seconds / 3600, 2)
                    message = f'Последний раз:\nПисала: {diffPipi} часов назад\nКакала: {diffKaka} часов назад'
                    msg.reply(message)
                    return
                
                msg.reply(constants.ERROR)
            except Exception as e:
                msg.reply(constants.ERROR)
                self.logger.error(e)
                return
        return handle
