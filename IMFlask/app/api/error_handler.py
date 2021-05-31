from flask import Blueprint, jsonify, request
# from flask import render_template

error_handler = Blueprint("error_handler", __name__)


@error_handler.app_errorhandler(400)
def bad_request(error):
    """400 Error Handler"""
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        return jsonify(msg=str(error)), 400
    return '<h1>400 Page</h1>', 400


@error_handler.app_errorhandler(404)
def not_found(error):
    """404 Error Handler"""
    if request.accept_mimetypes.accept_json and \
       not request.accept_mimetypes.accept_html:
        return jsonify(msg=str(error)), 404
    return "<h1>404 page</h1>", 404


@error_handler.app_errorhandler(500)
def internal_server_error(error):
    """500 Error Handler"""
    if request.accept_mimetypes.accept_json and \
       not request.accept_mimetypes.accept_html:
        return jsonify(msg=str(error)), 500
    return "<h1>Internal Server Error</h1>", 500