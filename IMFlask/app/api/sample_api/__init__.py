"""
Sample API Module Package
"""
from flask import Blueprint

sample_api = Blueprint('sample_api')

from . import calcurator