# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

import hashlib
from Backend.DB.DBConn import db
from Backend.Utils.BackendUtils import *
from Backend.Utils.SysConstant import *
from Backend.DB.Model.UserSessionModel import UserSession
from Backend.DB.Model.UserModel import User

def register(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:

        user = User()
        user.Tel = param['tel']
        user.Name = param['name']
        user.Pwd = hashlib.md5(param['pwd']).hexdigest()
        (status, userSession) = checkRandomCodeIsValid(user.Tel)
        if status:
            # createSigKey
            (status, output) = sigKey(0, user.Name, APP_ID)
            if status == 0:
                user.SigKey = output
                RETURNVALUE[CODE] = status
                db.session.add(user)

                # Allocation PPDeviceID
                allocationPPDeviceID(user, 0)
            else:
                RETURNVALUE[MESSAGE] = output
        else:
            RETURNVALUE[MESSAGE] = "Random code invalid, Please get it again."
            RETURNVALUE[CODE] = 1

        db.session.delete(userSession)

        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = 1
        RETURNVALUE[MESSAGE] = e.message
        return buildReturnValue(RETURNVALUE)


def login(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        user = User.query.filter(User.Tel == param['tel']).first()
        if user is None:
            RETURNVALUE[MESSAGE] = "user does not exist."
            RETURNVALUE[CODE] = 1
        else:
            if user.Pwd != hashlib.md5(param['pwd'].hexdigest()):
                RETURNVALUE[MESSAGE] = "User validation failure."
                RETURNVALUE[CODE] = 1
            else:
                data = {}
                data['sigKey'] = user.SigKey
                RETURNVALUE[VALUE].append(data)

        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        RETURNVALUE[CODE] = 1
        RETURNVALUE[MESSAGE] = e.message
        return buildReturnValue(RETURNVALUE)


def updatePwd(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        user = User.query.filter(User.Tel == param['tel']).first()
        if user is None:
            RETURNVALUE[MESSAGE] = "user does not exist."
            RETURNVALUE[CODE] = 1
        else:
            if user.Pwd != param['oldPwd']:
                RETURNVALUE[MESSAGE] = "User validation failure."
                RETURNVALUE[CODE] = 1
            else:
                user.Pwd = param['newPwd']

        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = 1
        RETURNVALUE[MESSAGE] = e.message
        return buildReturnValue(RETURNVALUE)


def getRandomCode(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        # create Random Code
        randomCode = createPhoneCode()

        # send Random Code
        code = []
        code.append(randomCode)
        code.append(RANDOM_CODE_TIMEOUT)
        result = senMessage(code, param['tel'])

        if result['result'] == 0:
            userSession = UserSession.query.filter(UserSession.Tel == param['tel']).first()
            if userSession is None:
                userSession = UserSession()

            #save random code
            userSession.Tel = param['tel']
            userSession.RandomCode = randomCode
            db.session.add(userSession)
        else:
            RETURNVALUE[CODE] = 1
            RETURNVALUE[MESSAGE] = result['errmsg']
        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = 1
        RETURNVALUE[MESSAGE] = e.message
        return buildReturnValue(RETURNVALUE)