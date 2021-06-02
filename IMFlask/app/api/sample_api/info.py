"""
Get API
"""
from flask import g, jsonify
from flask_validation_extended import Json, Validator
from app.api import response, bad_request
from app.api.sample_api import sample_api as api
from app.api.decorator import timer
from model.mongodb import MasterConfig, Log


@api.route('/log')
@timer
def get_log_api():
    return response(Log(g.db).get_log(0, 10))


@api.route('/author')
@timer
def get_author_api():
    return response(MasterConfig(g.db).get_author())


@api.route('/author', methods=['POST', 'PUT'])
@Validator(bad_request)
def change_author_api(
    name=Json(str)
):
    MasterConfig(g.db).change_author(name)
    return response()



@api.route('/jsonify')
def get_jsonify_api():
    return jsonify(msg='성공!')