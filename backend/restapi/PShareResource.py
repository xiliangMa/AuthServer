# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from flask.ext.restful import Resource, reqparse
from FlaskManager import httpAuth
from PShareResourceImpl import addPShare, getPShares, updatePShare, removePShare


class addPShareAPI(Resource):
    @httpAuth.login_required
    def post(self):
        params = reqparse.RequestParser()
        params.add_argument("nasId", type = int, location = "json", required = True)
        params.add_argument("shareId", type = int, location = "json", required = False)
        params.add_argument("name", type = str, location = "json", required = True)
        params.add_argument("tel", type = int, location = "json", required = True)
        params.add_argument("heat", type = int, location = "json", required = False)
        return addPShare(params.parse_args())


class getPSharesAPI(Resource):
    @httpAuth.login_required
    def post(self):
        params = reqparse.RequestParser()
        params.add_argument("page", type = int, location = "json", required = False)
        params.add_argument("limit", type = int, location = "json", required = False)
        params.add_argument("sortField", type = int, location = "json", required = False)
        params.add_argument("sortType", type = int, location = "json", required = False)
        return getPShares(params.parse_args())


class updatePShareAPI(Resource):
    @httpAuth.login_required
    def put(self, shareId, nasId):
        params = reqparse.RequestParser()
        params.add_argument("isHeat", location = "json", required = True)
        return updatePShare(shareId, nasId, params.parse_args())


class removePShareAPI(Resource):
    @httpAuth.login_required
    def delete(self, shareId, nasId):
        return removePShare(shareId, nasId)