# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from flask.ext.restful import Resource, reqparse
from FlaskManager import httpAuth
from PShareResourceImpl import addShare


class addShareAPI(Resource):
    @httpAuth.login_required
    def post(self):
        params = reqparse.RequestParser()
        params.add_argument("nasId", type = int, location = "json", required = True)
        params.add_argument("shareId", type = int, location = "json", required = False)
        params.add_argument("name", type = str, location = "json", required = True)
        params.add_argument("tel", type = int, location = "json", required = True)
        params.add_argument("heat", type = int, location = "json", required = False)
        return addShare(params.parse_args())