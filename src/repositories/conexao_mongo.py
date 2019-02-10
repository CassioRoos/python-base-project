from pymongo import MongoClient

from configurations import config


class ConexaoMongo():
    def __init__(self):
        self._client = MongoClient(config.DB_URL, config.DB_PORTA)
        self.db = self._client[config.DB_NOME]
