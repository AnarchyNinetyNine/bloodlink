#!/usr/bin/python3
"""Create the Blueprint of Flask"""
from flask import Blueprint

app_views = Blueprint('api_views', __name__)


from api.v1.views.hospitals import *
