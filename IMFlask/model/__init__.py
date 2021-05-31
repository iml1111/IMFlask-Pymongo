"""
Application Model
"""
from config import APP_NAME
from model import mongodb


def init_app(config):
    """Model Init Function"""

    # MongoDB Init
    uri = config.MONGODB_URI
    initializer = mongodb.ModelInitializer(uri)
    initializer.init_model()
    print("[%s] MongoDB Initialization Completed" % APP_NAME)