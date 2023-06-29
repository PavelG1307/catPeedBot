from threading import Thread
import time
from bot import Bot
import constants
import utils
from pyrogram import Client
from pyrogram.types import Message
from logger import Logger
from user import User

class CustomHandler:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.users = []
        self.thread = Thread(target=self.runPhantom)
        self.thread.start()

    def getMsgHandler(self, bot: Bot):
        keyboard = utils.getKeyboard()
        self.bot = bot

        def handle(app: Client, msg: Message):
            user = self.getUser(msg.from_user.id)
            try:
                if msg.text == '/start':
                    msg.reply(constants.START_MESSAGE, reply_markup=keyboard)
                    return
                
                if msg.text == constants.KAKA_BTN_TEXT:
                    message = utils.getFormattedMessage(user.lastKaka)
                    user.updateKaka()
                    msg.reply(message, reply_markup=keyboard)
                    return
                
                if msg.text == constants.PIPI_BTN_TEXT:
                    message = utils.getFormattedMessage(user.lastPipi)
                    user.updatePipi()
                    msg.reply(message, reply_markup=keyboard)
                    return
                
                if msg.text == constants.CHECK_BTN_TEXT:
                    message = utils.getFormattedStatusMessage(user.lastPipi, user.lastKaka)
                    msg.reply(message, reply_markup=keyboard)
                    return
                
                msg.reply(constants.ERROR, reply_markup=keyboard)
            except Exception as e:
                msg.reply(constants.ERROR, reply_markup=keyboard)
                self.logger.error(e)
                return
        return handle

    def getUser(self, id: int) -> User:
        for user in self.users:
            if user.id == id:
                return user
        user = User(id)
        self.users.append(user)
        return user
    
    def runPhantom(self):
        while(True):
            time.sleep(3 * 60 * 60)
            try:
                self.performJob()
            except Exception as e:
                self.logger.error(e)

    def performJob(self):
        self.logger.info('Started performJob')

        for user in self.users:
            isNeedKaka = utils.checkTime(user.lastKaka)
            isNeedPipi = utils.checkTime(user.lastPipi)

            if not isNeedKaka and not isNeedPipi:
                continue
            try:
                self.bot.send_message(user.id, constants.WARNING)
            except Exception as e:
                self.logger.error(e)

        self.logger.info('Stopped performJob')
