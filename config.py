import dotenv
import os
import constants

dotenv.load_dotenv(constants.ENV_FILE_PATH)

class Config:
    bot_token: str
    bot_api_id: str
    bot_api_hash: str
    rollbar_is_enable: bool
    rollbar_token: str
    env: str
    logger_level: str
    code_version: str
    def __init__(self):
        self.bot_token = self.getFromEnv('BOT_TOKEN')
        self.bot_api_id = self.getFromEnv('BOT_API_ID')
        self.bot_api_hash = self.getFromEnv('BOT_API_HASH')
        self.rollbar_token = self.getFromEnv('ROLLBAR_TOKEN')
        self.rollbar_is_enable = bool(self.rollbar_token)
        self.env = self.getOrDefaultFromEnv('ENV', 'dev')
        self.logger_level = self.getOrDefaultFromEnv('LOGGER_LEVEL', 'info')
        self.code_version = self.getFromEnv('VERSION')

    def getFromEnv(self, key):
        return os.getenv(key)
    
    def getOrDefaultFromEnv(self, key, default):
        value = self.getFromEnv(key)
        if not value:
            return default
        return value