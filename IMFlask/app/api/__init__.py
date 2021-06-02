"""
API Request Handler and util
"""
from flask import g, current_app, request, Response
from model import mongodb
from model.mongodb import Log


def init_app(app):

    @app.before_first_request
    def before_first_request():
        pass

    @app.before_request
    def before_request():
        config = current_app.config
        # DB Connection
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

        # API Logging
        if config['API_LOGGING']:
            if isinstance(response, Response):
                status_code = response.status_code
            else:
                status_code = response[1]

            Log(g.db).insert_log({
                'ipv4': request.remote_addr,
                'url': request.full_path,
                'method': request.method,
                'params': request.data.decode(),
                'status_code': status_code
            })

        return response

    @app.teardown_request
    def teardown_request(exception):
        # DB Connection Close
        db = g.pop('db', None)
        if db:
            db.close()

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        pass


def response(result=None):
    if result is None:
        return {'msg': 'success'}, 200
    else:
        return {'msg': 'success', 'result': result}, 200


def bad_request(description):
    return {'msg': 'fail', 'description': description}, 400