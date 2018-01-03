# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


import UsersResourceImpl
from flask import request
from FlaskManager import app, httpAuth


@app.route('/authserver')
@httpAuth.login_required
def index():
    return app.send_static_file('index.html')


@app.route('/authserver/api/user/<tel>/checktel', methods = ['GET'])
@httpAuth.login_required
def checkTel(tel):
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
    return UsersResourceImpl.checkTel(tel)


@app.route('/authserver/api/user/register', methods = ['POST'])
@httpAuth.login_required
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
                            "type": (necessary = TRue) 0 app 1 nas
                          }

    @apiParamExample {json} Request-Example:
                          {
                            "tel":18701656257,
                            "pwd": "abc123",
                            "randomCode": 3333,
                            "type": 0
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
    return UsersResourceImpl.register(request.json)


@app.route('/authserver/api/user/login', methods = ['GET'])
@httpAuth.login_required
def login():
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
    return UsersResourceImpl.login(request.authorization)


@app.route('/authserver/api/user/<tel>/updatepwd', methods = ['PUT'])
@httpAuth.login_required
def updatePwd(tel):
    """
    @api {put} /api/user/<tel>/updatepwd
    @apiVersion 1.0.0
    @apiName updatepwd
    @apiGroup user
    @apiDescription  Update user pwd

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
    return UsersResourceImpl.updatePwd(tel, request.json)


@app.route('/authserver/api/user/<tel>/getrandomcode', methods = ['GET'])
@httpAuth.login_required
def getRandomCode(tel):
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
    return UsersResourceImpl.getRandomCode(tel)


if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)



