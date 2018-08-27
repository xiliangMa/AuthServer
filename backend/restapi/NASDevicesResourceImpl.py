# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from backend.utils.LogManager import Log
from backend.errors import BackendErrorCode, BackendErrorMessage
from backend.utils.BackendUtils import dbRollback, buildReturnValue
from backend.utils.SysConstant import VALUE, CODE, MESSAGE
from FlaskManager import db
from backend.model.UserNASModel import UserNAS


logManager = Log()
log = logManager.getLogger("NASDevicesResourcesImpl")

def bindUserNAS(param, nasId, tel):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None

    try:
        userNas = UserNAS.query.filter(UserNAS.NasId == nasId, UserNAS.Tel == tel).first()
        if userNas is not None:
            RETURNVALUE[CODE] = BackendErrorCode.NAS_USER_IS_BIND_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.NAS_USER_IS_BIND_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)
        userNas = UserNAS()
        userNas.Tel = tel
        userNas.NasId = nasId
        userNas.IsAdmin = param['isAdmin']
        db.session.add(userNas)

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = e
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)


def removeUserNAS(nasId, tel):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None

    try:
        userNas = UserNAS.query.filter(UserNAS.NasId == nasId, UserNAS.Tel == tel).first()
        if userNas is None:
            RETURNVALUE[CODE] = BackendErrorCode.NAS_IS_NOT_BIND_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.NAS_IS_NOT_BIND_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        UserNAS.query.filter(UserNAS.NasId == nasId, UserNAS.Tel == tel).delete()

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)
    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = e
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)