# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

import hashlib

from backend.model.UserModel import User
from backend.model.UserSessionModel import UserSession
from backend.model.NASDevicesModel import NASDevices
from backend.model.UserNASModel import UserNAS
from backend.utils.BackendUtils import checkRandomCodeIsValid, buildReturnValue, allocationPPDeviceID
from backend.utils.BackendUtils import createPhoneCode, senMessage, dbRollback, sigKey, updateIpToNumber
from backend.utils.SysConstant import VALUE, CODE, MESSAGE, APP_ID, RANDOM_CODE_TIMEOUT
from backend.errors import BackendErrorCode, BackendErrorMessage
from backend.utils.SysConstant import ADMIN
from backend.utils.LogManager import Log
from FlaskManager import db
import time, datetime


logManager = Log()
log = logManager.getLogger("UsersResourcesImpl")

def register(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        mobile =  str(param['areaCode']) + str(param['tel'])
        type = param['type']
        #check user is registered
        user = User.query.filter(User.Tel == mobile).first()
        if user is not None:
            if type == 1:
                user.Pwd = hashlib.md5(param['pwd']).hexdigest()
                RETURNVALUE[VALUE].append(user.SigKey)
                log.info(RETURNVALUE)
                return buildReturnValue(RETURNVALUE)

            RETURNVALUE[CODE] = BackendErrorCode.USER_IS_REGISTERED_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.USER_IS_REGISTERED_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        user = User()
        user.Tel = mobile
        user.Pwd = hashlib.md5(param['pwd']).hexdigest()
        user.Email = param['email']
        user.Name = param['name']


        if type == 0:
            randomCode = param['randomCode']
            # chec random code
            (userSession, errorCode, errorMessage) = checkRandomCodeIsValid(user.Tel, randomCode)
            if errorCode != 0:
                RETURNVALUE[CODE] = errorCode
                RETURNVALUE[MESSAGE] = errorMessage
                log.error(RETURNVALUE)
                return buildReturnValue(RETURNVALUE)
        else:
            nasDevices = NASDevices()
            nasDevices.NasId = mobile
            nasDevices.IP = updateIpToNumber(param['ip'])
            nasDevices.MAC = param['mac']


        # Allocation PPDeviceID
        iReqID = allocationPPDeviceID(user, 0, user.Tel)
        if iReqID < 0 and iReqID != -17:
            RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
            RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)


        # createSigKey
        (errorCode, output) = sigKey(0, mobile, APP_ID)
        if errorCode != 0:
            RETURNVALUE[MESSAGE] = output
            RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        # add user
        user.SigKey = output
        db.session.add(user)

        # add nas
        if type == 1:
            db.session.add(nasDevices)

        # remove userSession
        if type == 0:
            db.session.delete(userSession)
        RETURNVALUE[VALUE].append(user.SigKey)
        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)


def login(auth):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        if auth.username != ADMIN:
            user = User.query.filter(User.Tel == auth.username).first()
            timeInterval = 12960000 #24 * 60 * 60 * 5 * 30
            if (int(time.time()) - int(time.mktime(time.strptime(str(user.CreateTime), "%Y-%m-%d %H:%M:%S")))) > timeInterval:
                log.error("CheckSigKey: User %s sigkey invalid, time- %s", str(user.Tel), user.CreateTime)
                (errorCode, output) = sigKey(0, user.Tel, APP_ID)
                if errorCode != 0:
                    RETURNVALUE[MESSAGE] = output
                    RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
                    log.error("CheckSigKey: user %s sigkey create failed.", str(user.Tel))
                    return buildReturnValue(RETURNVALUE)
                log.info("CheckSigKey: user %s sigkey create success.", str(user.Tel))
                user.SigKey = output
                user.CreateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            data = {}
            data['sigKey'] = user.SigKey
            RETURNVALUE[VALUE].append(data)

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
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
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        # check randomCode
        (userSession, errorCode, errorMessage) = checkRandomCodeIsValid(user.Tel, param['randomCode'])
        if errorCode != 0:
            RETURNVALUE[MESSAGE] = errorMessage
            RETURNVALUE[CODE] = errorCode
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        # update pwd
        user.Pwd = hashlib.md5(param['newPwd']).hexdigest()

        # remove userSession
        db.session.delete(userSession)

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)


def getRandomCode(areacode, tel):
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
        sendMessage = senMessage(code, areacode, tel)

        log.info(sendMessage)
        if sendMessage['result'] != 0:
            RETURNVALUE[MESSAGE] = sendMessage['errmsg']
            RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        mobile = str(areacode) + str(tel)
        userSession = UserSession.query.filter(UserSession.Tel == mobile).first()
        if userSession is None:
            userSession = UserSession()

        # save random code
        userSession.Tel = mobile
        userSession.RandomCode = randomCode
        db.session.add(userSession)

        # build return value
        data = {}
        data['randomCode'] = randomCode
        RETURNVALUE[VALUE].append(data)

        log.info(RETURNVALUE)

        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
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

        if RETURNVALUE[CODE] == 0:
            log.info(RETURNVALUE)
        else:
            log.error(RETURNVALUE)

        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)


def getUserNASDevices(tel):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None

    try:
        UserNASList = UserNAS.query.filter(UserNAS.Tel == tel).all()
        for data in UserNASList:
            userNas = {}
            userNas['tel'] = data.Tel
            userNas['nasId'] = data.NasId
            userNas['isAdmin'] = data.IsAdmin
            RETURNVALUE[VALUE].append(userNas)

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)