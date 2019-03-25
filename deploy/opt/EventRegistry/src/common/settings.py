# Internal
from src.data_source.config.config_file import ConfigFile


class Settings:

    def __init__(self, settingsProvider):

        self.__settingsProvider = settingsProvider


    def __getattr__(self, item):

        return getattr(self.__settingsProvider, item)


settings = Settings(settingsProvider = ConfigFile())