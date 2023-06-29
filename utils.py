import constants
from datetime import datetime, timedelta
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

def getFormattedStatusMessage(lastPipi, lastKaka): 
    now = datetime.now()
    pipiMsg = 'Писала 💦: Нет данных 😒'
    kakaMsg = 'Какала 💩: Нет данных 😒'

    if not lastPipi is None:
        diffPipi = round((now - lastPipi).seconds / 3600, 2)
        pipiMsg = f'Писала 💦: {diffPipi} часов назад'
    if not lastKaka is None:
        diffKaka = round((now - lastKaka).seconds / 3600, 2)
        kakaMsg = f'Какала 💩: {diffKaka} часов назад'
    return f'Последний раз:\n{pipiMsg}\n{kakaMsg}'

def getFormattedMessage(lastTime):
    if lastTime is None:
        return constants.FIRST_TIME
    now = datetime.now()
    diff = now - lastTime
    countHrs = round(diff.seconds / 3600, 2)
    return f'Ей/ему потребовалось {countHrs} часов чтобы сделать это!'

def getKeyboard():
    pipiBtn = KeyboardButton(constants.PIPI_BTN_TEXT)
    kakaBtn = KeyboardButton(constants.KAKA_BTN_TEXT)
    checkBtn = KeyboardButton(constants.CHECK_BTN_TEXT)
    return ReplyKeyboardMarkup([[pipiBtn,kakaBtn], [checkBtn]])

def checkTime(time: datetime):
    if time is None:
        return False
    now = datetime.now()
    diffSeconds = (now - time).seconds
    return diffSeconds > 12 * 60 * 60