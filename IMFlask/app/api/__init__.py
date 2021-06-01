"""
API Request Handler and util
"""
from flask import abort, g, current_app, request
from app.controllers.log import insert_log
from model import mongodb


def init_app(app):

    @app.before_first_request
    def before_first_request():
        pass

    @app.before_request
    def before_request():
        config = current_app.config
        if config['TESTING'] is True:
            g.db = None
        else:
            g.db = mongodb.get_cursor(config['MONGODB_URI'])

    @app.after_request
    def after_request(response):
        config = current_app.config

        # Slow API Tracking
        if (
            'process_time' in g
            and g.process_time >= config['SLOW_API_TIME']
        ):
            log_str = "\n!!! SLOW API DETECTED !!! \n" + \
                      "ip: " + request.remote_addr + "\n" + \
                      "url: " + request.full_path + "\n" + \
                      "input_json: " + str(request.get_json()) + "\n" + \
                      "slow time: " + str(g.process_time) + "\n"
            app.logger.warning(log_str)

        # TODO: Api Tracking

        return response

    @app.teardown_request
    def teardown_request(exception):
        db = g.pop('db', None)
        if db:
            db.close()

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        pass