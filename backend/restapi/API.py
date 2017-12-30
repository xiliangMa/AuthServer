# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from flask.ext.restful import Api

from FlaskManager import app
from backend.restapi.APIDocResource import APIDoc
from backend.restapi.UserResource import getRandomCodeAPI, checTelAPI, registerAPI, loginAPI, updatePwdAPI


api = Api(app)

api.add_resource(APIDoc, '/authserver')


"""
 @api {get} /api/user/<tel>/checktel
 @apiVersion 1.0.0
 @apiName checktel
 @apiGroup user
 @apiDescription  Check tel whether or not it has been registered

 @apiSuccessExample {json} Success-Response:
                    {
                    "code": 0,
                    "message": "SUCCESS",
                    "value": ""
                    }
@apiErrorExample {json} Error-Response:
                    {
                    "code": 1,
                    "message": "The phone number has been registered.",
                    "value": ""
                    }
"""
api.add_resource(checTelAPI, '/authserver/api/user/<int:tel>/checktel', endpoint = "checktel")


"""
  @api {get} api/user/<tel>/getrandomcode
  @apiVersion 1.0.0
  @apiName getrandomcode
  @apiGroup user
  @apiDescription  Get random code

  @apiSuccessExample {json} Success-Response:
                     {
                     "code": 0,
                     "message": "SUCCESS",
                     "value": ""
                     }
 @apiErrorExample {json} Error-Response:
                     {
                     "code": 1,
                     "message": "",
                     "value": ""
                     }
"""
api.add_resource(getRandomCodeAPI, '/authserver/api/user/<int:tel>/getrandomcode', endpoint = 'getrandomcode')


"""
    @api {post} /api/user/register
    @apiVersion 1.0.0
    @apiName register
    @apiGroup user
    @apiDescription  User register

    @apiParam {Number} tel required = True
    @apiParam {String} pwd required = True
    @apiParam {Number} type required = True(0 app 1 nas)
    @apiParam {Number} randomCode (type=0 required = True, type=1 required = False)
    @apiParam {String} email required = False
    @apiParam {String} name required = False

    @apiParamExample {json} Request-Example:
                          {
                            "tel":18701656257,
                            "pwd": "abc123",
                            "randomCode": 3333,
                            "type": 0,
                            "email": "894244011@qq.com",
                            "name": "test"
                          }

    @apiSuccessExample {json} Success-Response:
                        {
                        "code": 0,
                        "message": "SUCCESS",
                        "value": ""
                        }
    @apiErrorExample {json} Error-Response:
                        {
                        "code": 1,
                        "message": "",
                        "value": ""
                        }
"""
api.add_resource(registerAPI, '/authserver/api/user/register', endpoint = 'register')


"""
    @api {get} /api/user/login
    @apiVersion 1.0.0
    @apiName login
    @apiGroup user
    @apiDescription  User login

    @apiSuccessExample {json} Success-Response:
                       {
                       "code": 0,
                       "message": "SUCCESS",
                       "value": ""
                       }
    @apiErrorExample {json} Error-Response:
                       {
                       "code": 1,
                       "message": "",
                       "value": ""
                       }
"""
api.add_resource(loginAPI, '/authserver/api/user/login', endpoint = 'login')


"""
   @api {put} /api/user/<tel>/updatepwd
   @apiVersion 1.0.0
   @apiName updatepwd
   @apiGroup user
   @apiDescription  Update user pwd

    @apiParam {Number} tel required = True
    @apiParam {String} randomCode required = True

    @apiParamExample {json} Request-Example:
                         {
                           "newPwd": "abc123",
                           "randomCode": 3333
                         }

   @apiSuccessExample {json} Success-Response:
                      {
                      "code": 0,
                      "message": "SUCCESS",
                      "value": ""
                      }
   @apiErrorExample {json} Error-Response:
                      {
                      "code": 1,
                      "message": "",
                      "value": ""
                      }
"""
api.add_resource(updatePwdAPI, '/authserver/api/user/<int:tel>/updatepwd', endpoint = 'updatepwd')