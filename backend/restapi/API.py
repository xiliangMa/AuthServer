# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from flask.ext.restful import Api

from FlaskManager import app
from backend.restapi.APIDocResource import APIDoc
from backend.restapi.UserResource import getRandomCodeAPI, checTelAPI, registerAPI, loginAPI, updatePwdAPI, getUserNASDevicesAPI
from backend.restapi.PShareResource import addPShareAPI, getPSharesAPI, updatePShareAPI, removePShareAPI, removePShareByIDSAPI
from backend.restapi.NASDevicesResource import bindUserNASAPI, removeUserNASAPI


api = Api(app)

"""
    API Doc
"""
api.add_resource(APIDoc, '/authserver')

############################ User ############################

"""
 @api {get} /api/user/<tel>/checktel
 @apiVersion 1.0.0
 @apiName checktel
 @apiGroup User
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
  @api {get} /api/user/<tel>/getrandomcode
  @apiVersion 1.0.0
  @apiName getrandomcode
  @apiGroup User
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
    @apiGroup User
    @apiDescription  User register

    @apiParam {Number} tel required = True
    @apiParam {String} pwd required = True
    @apiParam {Number} type required = True(0 app 1 nas)
    @apiParam {Number} randomCode (type=0 required = True, type=1 required = False)
    @apiParam {String} email required = False
    @apiParam {String} name required = False
    @apiParam {String} ip required = False
    @apiParam {String} mac required = False

    @apiParamExample {json} Request-Example:
                          {
                            "tel":18701656257,
                            "pwd": "abc123",
                            "randomCode": 3333,
                            "type": 0,
                            "email": "894244011@qq.com",
                            "name": "test",
                            "ip": "1.1.1.1",
                            "mac": "00:1a:4a:6f:00:03"
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
    @apiGroup User
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
    @apiGroup User
    @apiDescription  Update user pwd

    @apiParam {String} newPwd required = True
    @apiParam {Number} randomCode required = True

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


"""
    @api {get} /api/user/<int:tel>/nas
    @apiVersion 1.0.0
    @apiName getUserNASDevices
    @apiGroup User
    @apiDescription  get User NAS Devices

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
api.add_resource(getUserNASDevicesAPI, '/authserver/api/user/<int:tel>/nas', endpoint = 'getUserNASDevices')


############################ PShare ############################
"""
    @api {post} /api/pshare
    @apiVersion 1.0.0
    @apiName addPShare
    @apiGroup PShare
    @apiDescription  add public share

    @apiParam {Number} nasId required = True
    @apiParam {Number} shareId required = True
    @apiParam {String} name required = True
    @apiParam {Number} tel required = True
    @apiParam {Number} heat required = False
    @apiParam {Number} type required = False
    @apiParam {String} notes required = False
    @apiParam {String} shareWith required = False
    @apiParam {String} Thumbnail required = False

    @apiParamExample {json} Request-Example:
                         {
                           "nasId": 12344544,
                           "shareId": 1,
                           "name": "share1",
                           "pwd": "abc123",
                           "tel": 18701656257,
                           "heat": 100,
                           "type": 1,
                           "notes": "note1",
                           "shareWith": {"shares":[{"shareId":1,"shareWith": "zhangsan"},{"shareId": 2,"shareWith": "lisi"}]},
                           "thumbnail": ""
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
api.add_resource(addPShareAPI, '/authserver/api/pshare', endpoint = 'addpshare')


"""
    @api {post} /api/pshares
    @apiVersion 1.0.0
    @apiName getPShares
    @apiGroup PShare
    @apiDescription  get public shares

    @apiParam {Number} page required = False, default 1
    @apiParam {Number} limit required = False, default 20
    @apiParam {Number} sortField required = False, (default 0, name 0, createTime 1, heat 2)
    @apiParam {Number} sortType required = Flase, (default asce, asce 0, desc 1)
    @apiParam {Number} type required = False
    @apiParam {String} shareWith required = False, (Fuzzy query: true)
    @apiParam {Number} nasId required = False
    @apiParam {Number} tel required = Flase
    @apiParam {String} name required = Flase, (Fuzzy query: false)

    @apiParamExample {json} Request-Example:
                 {
                   "page": 1,
                   "limit": 20,
                   "sortField": 0,
                   "sortType": 1,
                   "type": 1,
                   "shareWith": "zhangsan,lisi",
                   "nasId": 1,
                   "tel": 18701656257,
                   "name": "share1"
                 }

    @apiSuccessExample {json} Success-Response:
              {
                  "code": 0, 
                  "message": "SUCCESS", 
                  "value": [
                    {
                      "createTime": "2018-04-11 16:53:16", 
                      "heat": 100, 
                      "name": "share1", 
                      "nasId": 1, 
                      "id": 1,
                      "shaeId": 1, 
                      "shareWith": {"shares":[{"shareId":1,"shareWith": "zhangsan"},{"shareId": 2,"shareWith": "lisi"}]}", 
                      "tel": 18701656257, 
                      "type": 1001,
                      "thumbnail": "base64字节"
                    }
                  ]
                }
              }
    @apiErrorExample {json} Error-Response:
             {
              "code": 1,
              "message": "",
              "value": ""
              }
"""
api.add_resource(getPSharesAPI, '/authserver/api/pshares', endpoint = 'getpshares')


"""
    @api {put} /api/pshare/<int:id>
    @apiVersion 1.0.0
    @apiName updatePShare
    @apiGroup PShare
    @apiDescription  update public share

    @apiParam {Number} id required = True


    @apiSuccessExample {json} Success-Response:
                      {
                      "code": 0,
                      "message": "SUCCESS",
                      "value": []
                    }
    @apiErrorExample {json} Error-Response:
                     {
                      "code": 1,
                      "message": "",
                      "value": ""
                      }
"""
api.add_resource(updatePShareAPI, '/authserver/api/pshare/<int:id>', endpoint = 'updatePShare')


"""
    @api {post} /api/pshares/removepshare
    @apiVersion 1.0.0
    @apiName removePShares
    @apiGroup PShare
    @apiDescription  remove public shares

    
    @apiParam {Number} type required = False
    @apiParam {Number} nasId required = False
    @apiParam {String} shareWith required = False
    @apiParam {Number} shareId required = Flase
    
     @apiParamExample {json} Request-Example:
                {"params": 
                   {"pshares":[
                            {"nasId": 2, "shareId": 1,"type": 1,"shareWith": {"shares":[{"shareId":1,"shareWith": "zhangsan"},{"shareId": 2,"shareWith": "lisi"}]}},
                            {"nasId": 2, "shareId": 1,"type": 1,"shareWith": {"shares":[{"shareId":1,"shareWith": "zhangsan"},{"shareId": 2,"shareWith": "lisi"}]}}
                        ]
                    }
                }


    @apiSuccessExample {json} Success-Response:
                      {
                      "code": 0,
                      "message": "SUCCESS",
                      "value": []
                    }
    @apiErrorExample {json} Error-Response:
                     {
                      "code": 1,
                      "message": "",
                      "value": ""
                      }
"""
api.add_resource(removePShareAPI, '/authserver/api/pshares/removepshare', endpoint = 'removePShare')


"""
    @api {post} /api/pshares/removeByIds
    @apiVersion 1.0.0
    @apiName removePShareByIds
    @apiGroup PShare
    @apiDescription  remove public shares by ids

    
    @apiParam {String} ids required = False
    
     @apiParamExample {json} Request-Example:
                 {
                   "ids": "1,2,3"
                 }


    @apiSuccessExample {json} Success-Response:
                      {
                      "code": 0,
                      "message": "SUCCESS",
                      "value": []
                    }
    @apiErrorExample {json} Error-Response:
                     {
                      "code": 1,
                      "message": "",
                      "value": ""
                      }
"""
api.add_resource(removePShareByIDSAPI, '/authserver/api/pshares/removeByIds', endpoint = 'removePShareByIds')


"""
    @api {post} /api/nas/<int:nasId>/user/<int:tel>
    @apiVersion 1.0.0
    @apiName bindNASDevices
    @apiGroup Nas
    @apiDescription  User bind Nas Devices

    @apiParam {Number} nasId isAdmin = True (0 false, 1 true)
    
    @apiParamExample {json} Request-Example:
                         {
                           "isAdmin": 0
                         }
                         
    @apiSuccessExample {json} Success-Response:
                      {
                      "code": 0,
                      "message": "SUCCESS",
                      "value": []
                    }
    @apiErrorExample {json} Error-Response:
                     {
                      "code": 1,
                      "message": "",
                      "value": ""
                      }
"""
api.add_resource(bindUserNASAPI, '/authserver/api/nas/<int:nasId>/user/<int:tel>', endpoint = 'bindNASDevices')


"""
    @api {delete} /api/nas/<int:nasId>/user/<int:tel> 
    @apiVersion 1.0.0
    @apiName removeNASDevices
    @apiGroup Nas
    @apiDescription  User dissolve Nas Devices
    
    @apiSuccessExample {json} Success-Response:
                      {
                      "code": 0,
                      "message": "SUCCESS",
                      "value": []
                    }
    @apiErrorExample {json} Error-Response:
                     {
                      "code": 1,
                      "message": "",
                      "value": ""
                      }
"""
api.add_resource(removeUserNASAPI, '/authserver/api/nas/<int:nasId>/user/<int:tel>', endpoint = 'removeNASDevices')