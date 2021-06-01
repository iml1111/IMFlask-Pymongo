from datetime import datetime
from model.mongodb import Model


class MasterConfig(Model):

    VERSION = 1

    @property
    def index(self) -> list:
        return []

    @property
    def schema(self) -> dict:
        return {
            'config_type': None,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            '__version__': self.VERSION,
        }

    def get_author(self, proj=None):
        return self.col.find_one({'author_type': 'author'}, proj)

    def change_author(self, author: str):
        self.col.update(
            {'author_type': 'author'},
            {
                '$set': {
                    '__author__': author,
                    'updated_at': datetime.now()
                }
            }
        )