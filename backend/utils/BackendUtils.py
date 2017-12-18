# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

import commands
import os
import random
import time
from flask import jsonify
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

from backend.model.UserSessionModel import UserSession
from backend.model.NASDevicesModel import NASDevices
from backend.model.PPDevicesModel import PPDevices
from backend.model.UserModel import User
from backend.utils.SysConstant import *
from DBConn import db

'''
   返回参数
   {"code": "",
    "message": "",
    "value": ""}
'''


def buildReturnValue(RETURNVALUE):
    if RETURNVALUE[CODE] == 0:
        RETURNVALUE[CODE] = 0
        if RETURNVALUE[MESSAGE] is None:
            RETURNVALUE[MESSAGE] = 'SUCCESS'
        return jsonify(RETURNVALUE)
    else:
        RETURNVALUE[CODE] = 1
        if RETURNVALUE[MESSAGE] is None:
            RETURNVALUE[MESSAGE] = 'FAILED'
        return jsonify(RETURNVALUE)


'''
   @commType
        0 gen
        1 verify
   ./tls_licence_tools gen 私钥文件路径 sig将要存放的路径 sdkappid 用户id（用户名）
'''
tlsPath = os.path.abspath(os.path.dirname("AuthServer.py")) + tlsDir
def sigKey(commType, userName, sdkAppId):
    (status, output) = commands.getstatusoutput(buildSigKeyComm(commType, userName, sdkAppId))
    if status == 0:
        # get sigKey from file
        filePath = tlsPath + sdkAppId + "_" + userName + "_sig"
        (status, output) = getSigKey(filePath)
    return status, output


def buildSigKeyComm(commType, userName, sdkAppId):
    publicKey = tlsPath + PUBLIC_KEY
    ecKey = tlsPath + PRIVATE_KEY
    sig = tlsPath + sdkAppId + '_' + userName + '_sig'
    space = ' '

    if (commType == 0):
        type = 'tls_licence_tools gen'
        comm = tlsPath + type + space + ecKey + space + sig + space + sdkAppId + space + userName
    else:
        type = 'tls_licence_tools verify'
        comm = tlsPath + type + space + publicKey + space + sig + space + sdkAppId + space + userName

    return comm


def getSigKey(filePath):
    (status, output) = commands.getstatusoutput("cat " + filePath)
    return status, output


'''
    @type
        0 user
        1 nas
'''
def allocationPPDeviceID(object, type):
    pPDevices = PPDevices.query.filter(PPDevices.IsUsed == None).first()
    if type == 0:
        newObject = User.query.filter(User.Name == object.Name).first()
        if newObject is not None:
            pPDevices.IsUsed = newObject.Tel
    else:
        newObject = NASDevices.query.filter(NASDevices.NasId == object.NasId).first()
        if newObject is not None:
            pPDevices.IsUsed = newObject.NasId



def dbRollback(db):
    db.session.rollback()
    db.session.flush()


'''
    Generating four digit random code
'''
def createPhoneCode():
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    x = random.choice(chars), random.choice(chars), random.choice(chars), random.choice(chars)
    verifyCode = "".join(x)
    return verifyCode


'''
params : [5031, 4]
phone_numbers: 18701657257

'''

ssender = SmsSingleSender(APP_ID, APP_KEY)
def senMessage(params, phone_numbers):
    try:
        return ssender.send_with_param(86, phone_numbers, TEMPLATE_ID, params)
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)


def checkRandomCodeIsValid(tel):
    status = True
    localTime = time.time()
    userSession = UserSession.query.filter(UserSession.Tel == tel).first()
    print userSession.CreateTime
    createTime = time.mktime(time.strptime(str(userSession.CreateTime), '%Y-%m-%d %H:%M:%S'))
    timeDiff = (localTime - createTime)/60
    print timeDiff
    if (timeDiff > 5):
        db.session.delete(userSession)
        status = False
    return status, userSession




if __name__ == "__main__":
    checkRandomCodeIsValid('18701656257')
    pass
    # sigKey(1, 'maxl', '1255610113')
    # sigKey(1, 'test2', '1255610839')
    # getSigKey()