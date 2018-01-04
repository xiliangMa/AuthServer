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


def addPShare(param):
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


def getPShares(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        page = param['page']
        limit = param['limit']
        sortField = param['sortField']
        sortType = param['sortType']

        if page is None:
            page = 1

        if limit is None:
            limit = 20

        if sortField == 0 or sortField is None:
            sort = PShare.Name
        elif sortField == 1:
            sort = PShare.CreateTime
        elif sortField == 2:
            sort = PShare.HEAT
        else:
            RETURNVALUE[CODE] = BackendErrorCode.PSHARE_IS_EXIST_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.PSHARE_IS_EXIST_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        if sortType == 0 or sortType is None:
            # pshares = PShare.query.order_by(sort).limit(limit).all()
            datas = PShare.query.order_by(sort).paginate(page, limit, False).items
        else:
            # pshares = PShare.query.order_by(sort.desc()).limit(limit).all()
            datas = PShare.query.order_by(sort.desc()).paginate(page, limit, False).items

        # build return value
        for data in datas:
            print data.Name
            pshare = {}
            pshare['name'] = data.Name
            pshare['nasId'] = data.NasId
            pshare['shaeId'] = data.ShareId
            pshare['createTime'] = data.CreateTime.strftime('%Y-%m-%d %H:%M:%S')
            pshare['tel'] = data.Tel
            pshare['heat'] = data.HEAT
            RETURNVALUE[VALUE].append(pshare)

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)


def updatePShare(shareId, nasId, param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        isHeat = param['isHeat']
        pshare = PShare.query.filter(PShare.ShareId == shareId, PShare.NasId == nasId).first()

        if pshare is None:
            RETURNVALUE[CODE] = BackendErrorCode.PSHARE_NOT_EXIST_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.PSHARE_NOT_EXIST_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        if isHeat:
            pshare.HEAT = pshare.HEAT + 1

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)


def removePShare(shareId, nasId):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        PShare.query.filter(PShare.ShareId == shareId, PShare.NasId == nasId).delete()
        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)
    
    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)