# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

import hashlib

from backend.model.UserModel import User
from backend.utils.BackendUtils import *
from backend.utils.SysConstant import *
from backend.errors import BackendErrorCode


def register(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        #check user is registered
        user = User.query.filter(User.Tel == param['tel']).first()
        if user is not None:
            RETURNVALUE[CODE] = BackendErrorCode.USER_IS_REGISTERED_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.USER_IS_REGISTERED_ERROR
            return buildReturnValue(RETURNVALUE)

        user = User()
        user.Tel = param['tel']
        user.Pwd = hashlib.md5(param['pwd']).hexdigest()
        randomCode = param['randomCode']
        # chec random code
        (userSession, errorCode, errorMessage) = checkRandomCodeIsValid(user.Tel, randomCode)
        if errorCode != 0:
            RETURNVALUE[CODE] = errorCode
            RETURNVALUE[MESSAGE] = errorMessage
            return buildReturnValue(RETURNVALUE)

        # createSigKey
        (errorCode, output) = sigKey(0, user.Tel, APP_ID)
        if errorCode != 0:
            RETURNVALUE[MESSAGE] = output
            RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
            return buildReturnValue(RETURNVALUE)

        # add user
        user.SigKey = output
        db.session.add(user)

        # Allocation PPDeviceID
        allocationPPDeviceID(user, 0, user.Tel)

        # remove userSession
        db.session.delete(userSession)

        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        return buildReturnValue(RETURNVALUE)


def login(tel, param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:

        user = User.query.filter(User.Tel == tel).first()
        if user is None:
            RETURNVALUE[MESSAGE] = BackendErrorMessage.USER_NOT_EXIST_ERROR
            RETURNVALUE[CODE] = BackendErrorCode.USER_NOT_EXIST_ERROR
            return buildReturnValue(RETURNVALUE)

        if user.Pwd != hashlib.md5(param['pwd']).hexdigest():
            RETURNVALUE[MESSAGE] = BackendErrorMessage.USER_PWD_ERROR
            RETURNVALUE[CODE] = BackendErrorCode.USER_PWD_ERROR
            return buildReturnValue(RETURNVALUE)

        data = {}
        data['sigKey'] = user.SigKey
        RETURNVALUE[VALUE].append(data)

        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        return buildReturnValue(RETURNVALUE)


def updatePwd(tel, param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        """
            TO DO
            validata old pwd model
        """
        # user = User.query.filter(User.Tel == param['tel']).first()
        # if user is None:
        #     RETURNVALUE[MESSAGE] = "user does not exist."
        #     RETURNVALUE[CODE] = 1
        # else:
        #     if user.Pwd != hashlib.md5(param['oldPwd']).hexdigest():
        #         RETURNVALUE[MESSAGE] = "User validation failure."
        #         RETURNVALUE[CODE] = 1
        #     else:
        #         user.Pwd = hashlib.md5(param['newPwd']).hexdigest()


        """
            randomCode model
        """
        user = User.query.filter(User.Tel == tel).first()

        if user is None:
            RETURNVALUE[MESSAGE] = BackendErrorMessage.USER_NOT_EXIST_ERROR
            RETURNVALUE[CODE] = BackendErrorCode.USER_NOT_EXIST_ERROR
            return buildReturnValue(RETURNVALUE)

        # check randomCode
        (userSession, errorCode, errorMessage) = checkRandomCodeIsValid(user.Tel, param['randomCode'])
        if errorCode != 0:
            RETURNVALUE[MESSAGE] = errorMessage
            RETURNVALUE[CODE] = errorCode
            return buildReturnValue(RETURNVALUE)

        # update pwd
        user.Pwd = hashlib.md5(param['newPwd']).hexdigest()

        # remove userSession
        db.session.delete(userSession)

        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        return buildReturnValue(RETURNVALUE)


def getRandomCode(tel):
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
        result = senMessage(code, tel)

        if result['result'] != 0:
            RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
            RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
            return buildReturnValue(RETURNVALUE)

        userSession = UserSession.query.filter(UserSession.Tel == tel).first()
        if userSession is None:
            userSession = UserSession()

        # save random code
        userSession.Tel = tel
        userSession.RandomCode = randomCode
        db.session.add(userSession)

        # build return value
        data = {}
        data['randomCode'] = randomCode
        RETURNVALUE[VALUE].append(data)

        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        return buildReturnValue(RETURNVALUE)


def checkTel(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None

    try:
        user = User.query.filter(User.Tel == param).first()
        if user is not None:
            RETURNVALUE[CODE] = BackendErrorCode.USER_IS_REGISTERED_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.USER_IS_REGISTERED_ERROR

        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        return buildReturnValue(RETURNVALUE)