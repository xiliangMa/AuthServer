# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from backend.utils.LogManager import Log
from backend.errors import BackendErrorCode, BackendErrorMessage
from backend.utils.BackendUtils import dbRollback, buildReturnValue
from backend.utils.SysConstant import VALUE, CODE, MESSAGE
from FlaskManager import db
from backend.model.PShareModel import PShare

logManager = Log()
log = logManager.getLogger("PShareResourcesImpl")


def addShare(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        pshare = PShare.query.filter(PShare.ShareId == param['shareId']).first()
        if pshare is not None:
            RETURNVALUE[CODE] = BackendErrorCode.PSHARE_IS_EXIST_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.PSHARE_IS_EXIST_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        pshare = PShare()
        pshare.Name = param['name']
        pshare.NasId = param['nasId']
        pshare.ShareId = param['shareId']
        pshare.Tel = param['tel']
        pshare.HEAT = param['heat']
        db.session.add(pshare)

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)