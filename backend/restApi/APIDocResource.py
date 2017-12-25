# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from flask.ext.restful import Resource, reqparse, abort
from FlaskManager import app

class APIDoc(Resource):

    def get(self):
        return app.send_static_file('index.html')
