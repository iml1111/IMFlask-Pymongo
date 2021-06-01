from abc import ABCMeta
from datetime import datetime
from pymongo import MongoClient
from config import config

# Collections
from .log import Log
from .master_config import MasterConfig
MODELS = [Log, MasterConfig]


def get_cursor(uri=config.MONGODB_URI) -> MongoClient:
    """Get MongoDB Cursor"""
    return MongoClient(uri)


class Model(metaclass=ABCMeta):

    VERSION = 1

    def __init__(self, client, db_name=config.MONGODB_NAME):
        if client:
            self.col = client[db_name][self.__class__.__name__]
        else:
            self.col = None

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
        if self.col:
            self.col.create_indexes(self.index)

    def schemize(self, document: dict) -> dict:
        """generate JSON scheme"""
        return {**self.schema, **document}


class ModelInitializer:

    def __init__(self):
        self.uri = config.MONGODB_URI
        self.db = config.MONGODB_NAME

    @property
    def cursor(self):
        return get_cursor(self.uri)

    def init_model(self):
        """Initializer All Process"""
        with self.cursor as cur:
            self.init_index(cur)
            self.init_hello(cur)

    @staticmethod
    def init_index(cur):
        """Create Indexes each Collection"""
        for model in MODELS:
            model(cur).create_index()

    @staticmethod
    def init_hello(cur):
        """Customize for you"""

