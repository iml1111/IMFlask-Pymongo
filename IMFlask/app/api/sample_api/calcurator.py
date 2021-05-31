"""
Calc API
"""
from flask import g
from app.api.sample_api import sample_api as api
# TODO: flask validation import

@api.route('/add')
def add_api():
    return "hello"