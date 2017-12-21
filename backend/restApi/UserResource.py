# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from flask.ext.restful import Resource, reqparse, abort
from backend.restApi.UsersResourcesImpl import register


class UserAPI(Resource):

    def get(self, tel):
        print '==================='+ tel
        return 'UserAPI get ' + tel



class UserListAPI(Resource):

    def get(self, tel):
        return 'UserLIstAPI get '

    def post(self):
        params = reqparse.RequestParser()
        params.add_argument('tel', type = str, location='json', required = True)
        params.add_argument('name', type = str, location='json', required = True)
        params.add_argument('pwd', type = str, location='json', required = True)
        params.add_argument('email', type = str, location='json', required = False)
        params.add_argument('randomCode', type = str, location='json', required = True)
        return register(params.parse_args())
