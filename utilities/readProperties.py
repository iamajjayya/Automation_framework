


import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Configuration', 'config.ini'))
config.read(config_path)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        Url = config.get('common info', 'baseURL')
        return Url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'userName')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'passWord')
        return password

