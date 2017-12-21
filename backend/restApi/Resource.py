# -*- coding: utf-8 -*-
__author__ = 'xiliangma'



from flask import request, send_file

import UsersResourcesImpl
from DBConn import app



@app.route('/authserver')
def index():
    return app.send_static_file('index.html')


@app.route('/authserver/api/user/<tel>/checktel', methods = ['GET'])
def checkTel(tel):
    """
     @api {get} /api/user/<tel>/checktel
     @apiVersion 1.0.0
     @apiName checktel
     @apiGroup user
     @apiDescription  Check tel whether or not it has been registered

     @apiParam {Number} tel necessary = True

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
    return UsersResourcesImpl.checkTel(tel)


@app.route('/authserver/api/user/register', methods = ['POST'])
def register():
    """
    @api {post} /api/user/register
    @apiVersion 1.0.0
    @apiName register
    @apiGroup user
    @apiDescription  User register


    @apiParam {json} param {
                            "tel": (necessary = True),
                            "pwd": (necessary = True),
                            "randomCode": (necessary = True),
                            "email": (necessary = False)
                          }
    @apiParamExample {json} Request-Example:
                          {
                            "tel":18701656257,
                            "pwd": "abc123",
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
    return UsersResourcesImpl.register(request.json)


@app.route('/authserver/api/user/<tel>/login', methods = ['POST'])
def login(tel):
    """
    @api {get} /api/user/<tel>/login
    @apiVersion 1.0.0
    @apiName login
    @apiGroup user
    @apiDescription  User login

    @apiParam {Number} tel necessary = True
    @apiParam {json} param {
                            "pwd": (necessary = True)
                          }

     @apiParamExample {json} Request-Example:
                          {
                            "pwd": "abc123"
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
    return UsersResourcesImpl.login(tel, request.json)


@app.route('/authserver/api/user/<tel>/updatepwd', methods = ['PUT'])
def updatePwd(tel):
    """
    @api {put} /api/user/<tel>/updatepwd
    @apiVersion 1.0.0
    @apiName login
    @apiGroup user
    @apiDescription  Update user pwd

    @apiParam {Number} tel necessary = True
    @apiParam {json} param {
                            "newPwd": (necessary = True),
                            "randomCode": (necessary = True)
                          }

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
    return UsersResourcesImpl.updatePwd(tel, request.json)


@app.route('/authserver/api/user/<tel>/getrandomcode', methods = ['GET'])
def getRandomCode(tel):
    """
     @api {get} api/user/<tel>/getrandomcode
     @apiVersion 1.0.0
     @apiName getrandomcode
     @apiGroup user
     @apiDescription  Get random code

     @apiParam {Number} tel necessary = True

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
    return UsersResourcesImpl.getRandomCode(tel)


if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)



