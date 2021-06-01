"""
Get API
"""
from flask import g
from app.api.sample_api import sample_api as api


@api.route('/author')
def get_author_api():
    return "hello"

@api.route('/log')
def get_log_api():
    return "hello"