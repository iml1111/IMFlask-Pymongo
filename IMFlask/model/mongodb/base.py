from abc import ABCMeta
from datetime import datetime
from pymongo import MongoClient
from config import config


class Model(metaclass=ABCMeta):

    VERSION = 1

    def __init__(self, client: MongoClient, db_name=config.MONGODB_NAME):
        self.col = client[db_name][self.__class__.__name__]

    @property
    def index(self) -> list:
        """Get Index List"""
        return []

    @property
    def schema(self) -> dict:
        """Get default document format"""
        return {
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            '__version__': self.VERSION,
        }

    def create_index(self) -> None:
        """Create indexes"""
        if self.index:
            self.col.create_indexes(self.index)

    def schemize(self, document: dict) -> dict:
        """Generate JSON scheme"""
        return {**self.schema, **document}