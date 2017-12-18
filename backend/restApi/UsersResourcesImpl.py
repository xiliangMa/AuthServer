# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

import hashlib

from backend.model.UserModel import User
from backend.utils.BackendUtils import *
from backend.utils.SysConstant import *


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
            if user.Pwd != hashlib.md5(param['pwd']).hexdigest():
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


def updatePwd(tel, param):
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
            if user.Pwd != hashlib.md5(param['oldPwd']).hexdigest():
                RETURNVALUE[MESSAGE] = "User validation failure."
                RETURNVALUE[CODE] = 1
            else:
                user.Pwd = hashlib.md5(param['newPwd']).hexdigest()

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
        result = senMessage(code, param)

        if result['result'] == 0:
            userSession = UserSession.query.filter(UserSession.Tel == param).first()
            if userSession is None:
                userSession = UserSession()

            #save random code
            userSession.Tel = param
            userSession.RandomCode = randomCode
            db.session.add(userSession)
            data = {}
            data['randomCode'] = randomCode
            RETURNVALUE[VALUE].append(data)
        else:
            RETURNVALUE[CODE] = 1
            RETURNVALUE[MESSAGE] = result['errmsg']
        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = 1
        RETURNVALUE[MESSAGE] = e.message
        return buildReturnValue(RETURNVALUE)


def checkTel(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None

    try:
        if User.query.filter(User.Tel == param).first() is not None:
            RETURNVALUE[CODE] = 0
            RETURNVALUE[MESSAGE] = "The phone number has been registered."
        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        RETURNVALUE[CODE] = 1
        RETURNVALUE[MESSAGE] = e.message
        return buildReturnValue(RETURNVALUE)