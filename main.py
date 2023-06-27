from config import Config
from logger import Logger
from bot import Bot
from handler import CustomHandler

def main():
    config = Config()
    logger = Logger(config.logger_level, config.rollbar_is_enable, config.rollbar_token, config.env, config.code_version)
    bot = Bot(
        config.bot_api_id,
        config.bot_api_hash,
        config.bot_token,
        logger
    )
    handler = CustomHandler(logger)
    msgHandler = handler.getMsgHandler(bot)
    bot.add_msg_handler(msgHandler)
    bot.start()
    bot.idle()


if __name__ == '__main__':
    main()