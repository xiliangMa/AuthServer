# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from flask.ext.restful import Resource, reqparse
from FlaskManager import httpAuth
from NASDevicesResourceImpl import bindUserNAS, removeUserNAS


class bindUserNASAPI(Resource):
    @httpAuth.login_required
    def post(self, nasId, tel):
        params = reqparse.RequestParser()
        params.add_argument("IsAdmin", type = int, location = "json", required = True)
        return bindUserNAS(params.parse_args(), nasId, tel)


class removeUserNASAPI(Resource):
    @httpAuth.login_required
    def delete(self, nasId, tel):
        return removeUserNAS(nasId, tel)