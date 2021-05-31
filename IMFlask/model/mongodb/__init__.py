# from pymongo import MongoClient
# from .log import Log
# from .master_config import MasterConfig
#
#
# def get_cursor(uri):
#     return MongoClient(uri)
#
#
# class ModelInitializer:
#
#     def __init__(self, uri):
#         self.uri = uri
#
#     @property
#     def cursor(self):
#         return get_cursor(self.uri)
#
#     def init_model(self):
#         with self.cursor as cur:
#             pass
#
#     @staticmethod
#     def init_indexes(cur):
#         """Create Indexes each Collection"""
#         collections = [Log, MasterConfig]

if __name__ == '__main__':
    import os
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    file_list = os.listdir(BASEDIR)
    model_list = []
    for file_i in file_list:
        if not file_i.startswith('__init__') and file_i.endswith('.py'):
            module = __import__(file_i[:-3])
            model = getattr(
                module,
                file_i[:-3]
                    .replace("_", " ")
                    .title()
                    .replace(" ", "")
            )
            model_list.append(model)
    # TODO: 모델 디스커버 함수로 만들어서 콜렉션 생성 자동화
    print(model_list)