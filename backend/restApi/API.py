# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from flask.ext.restful import Api

from FlaskManager import app
from backend.restApi.UserResource import UserAPI
from backend.restApi.UserResource import UserListAPI
from backend.restApi.APIDocResource import APIDoc

api = Api(app)

api.add_resource(APIDoc, '/authserver')
api.add_resource(UserAPI, '/authserver/api/user/<string:tel>/checktel', endpoint = "checktel")
api.add_resource(UserAPI, '/authserver/api/user/<string:tel>/getrandomcode', endpoint = 'getrandomcode')
api.add_resource(UserListAPI, '/authserver/api/users')