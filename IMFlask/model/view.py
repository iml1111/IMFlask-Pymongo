from model.mongodb import Log, MasterConfig
from model.mock import Mock

def get_log(cursor, _skip, _limit):
    if cursor:
        return Log(cursor).get_log(
            _skip, _limit,
            proj={
                '_id': 0,
                'ipv4': 1,
                'url': 1,
                'method': 1,
                'params': 1,
                'status_code': 1,
                'created_at': 1,
            }
        )
    else:
        return Mock.get_log(_skip, _limit)


