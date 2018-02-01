# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from flask.ext.restful import Resource, reqparse
from flask import request
from backend.restapi.UsersResourceImpl import checkTel, getRandomCode, login, register, updatePwd
from FlaskManager import httpAuth


class checTelAPI(Resource):
    @httpAuth.login_required
    def get(self, tel):
        return checkTel(tel)


class getRandomCodeAPI(Resource):
    @httpAuth.login_required
    def get(self, tel):
        return getRandomCode(tel)


class registerAPI(Resource):
    @httpAuth.login_required
    def post(self):
        params = reqparse.RequestParser()
        params.add_argument("tel", type = int, location = "json", required = True)
        params.add_argument("name", type = str, location = "json", required = False)
        params.add_argument("pwd", type = str, location = "json", required = True)
        params.add_argument("email", type = str, location = "json", required = False)
        params.add_argument("randomCode", type = int, location = "json", required = False)
        params.add_argument("type", type = int, location = "json", required = True)
        params.add_argument("ip", type = str, location = "json", required = False)
        params.add_argument("mac", type = str, location = "json", required = False)
        return register(params.parse_args())


class loginAPI(Resource):
    @httpAuth.login_required
    def get(self):
        return login(request.authorization)


class updatePwdAPI(Resource):
    @httpAuth.login_required
    def put(self, tel):
        params = reqparse.RequestParser()
        params.add_argument("newPwd", type = str, location = "json", required = True)
        params.add_argument("randomCode", type = int, location = "json", required = True)
        return updatePwd(tel, params.parse_args())
