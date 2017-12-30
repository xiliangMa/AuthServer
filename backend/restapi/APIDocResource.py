# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from flask.ext.restful import Resource
from FlaskManager import app
from FlaskManager import httpAuth


class APIDoc(Resource):

    @httpAuth.login_required
    def get(self):
        return app.send_static_file('index.html')
