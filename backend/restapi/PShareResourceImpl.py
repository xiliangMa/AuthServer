# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from backend.utils.LogManager import Log
from backend.errors import BackendErrorCode, BackendErrorMessage
from backend.utils.BackendUtils import dbRollback, buildReturnValue
from backend.utils.SysConstant import VALUE, CODE, MESSAGE
from FlaskManager import db
from flask import jsonify
from backend.model.PShareModel import PShare
from sqlalchemy import and_
import json, hashlib

logManager = Log()
log = logManager.getLogger("PShareResourcesImpl")


def addPShare(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        pshare = PShare.query.filter(PShare.ShareId == param['shareId'], PShare.NasId == param['nasId']).first()
        if pshare is not None:
            RETURNVALUE[CODE] = BackendErrorCode.PSHARE_IS_EXIST_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.PSHARE_IS_EXIST_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        pshare = PShare()
        pshare.Name = param['name']
        #pshare.Pwd = hashlib.md5(param['pwd']).hexdigest()
        pshare.Pwd = param['pwd']
        pshare.NasId = param['nasId']
        pshare.ShareId = param['shareId']
        pshare.Tel = param['tel']
        pshare.Type = param['type']
        #shareWith = param['shareWith'].replace("'", '"').replace("u", ' ')
        #pshare.ShareWith = shareWith
        #pshare.ShareWithHash = hash(shareWith)
        shareWith = param['shareWith'].replace("'", '"').replace("u", ' ')
        pshare.ShareWith = shareWith
        pshare.Notes = param['notes']
        pshare.HEAT = param['heat']
        pshare.Thumbnail = param['thumbnail']
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
        nasId = param['nasId']
        shareId = param['shareId']
        tel = param['tel']
        type = param['type']
        shareWith = param['shareWith']
        name = param['name']


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

        words = []
        if shareWith is not None:
            for x in shareWith.split(","):
                words.append("%" + x + "%")

        if nasId is None:
            nasIdFilter = PShare.NasId != 0
        else:
            nasIdFilter = PShare.NasId == nasId

        if shareId is None:
            shareIdFilter = PShare.ShareId != 0
        else:
            shareIdFilter = PShare.ShareId == shareId

        if tel is None:
            telFilter = PShare.Tel != 0
        else:
            telFilter = PShare.Tel == tel

        if type is None:
            typeFilter = PShare.Type != 0
        else:
            typeFilter = PShare.Type == type


        nameFilter = PShare.Name == name


        rule = and_(*[PShare.ShareWith.like(w) for w in words])
        if sortType == 0 or sortType is None:
            # pshares = PShare.query.order_by(sort).limit(limit).all()
            # datas = PShare.query.filter(PShare.Name == name if name is not None else "*", PShare.NasId == nasId if nasId is not None else "*", PShare.Tel == tel if tel is not None else "*", PShare.Type == type if type is not None else "*").filter(rule).order_by(sort.desc()).paginate(page, limit, False).items
            if name is None:
                datas = PShare.query.filter(nasIdFilter, shareIdFilter, telFilter, typeFilter).filter(rule).order_by(sort.desc()).paginate(page, limit, False).items
            else:
                datas = PShare.query.filter(nasIdFilter, shareIdFilter, telFilter, typeFilter, nameFilter).filter(rule).order_by(sort.desc()).paginate(page, limit, False).items
        else:
            if name is None:
                datas = PShare.query.filter(nasIdFilter, shareIdFilter, telFilter, typeFilter).filter(rule).order_by(sort.desc()).paginate(page, limit, False).items
            else:
                datas = PShare.query.filter(nasIdFilter, shareIdFilter, telFilter, typeFilter, nameFilter).filter(rule).order_by(sort.desc()).paginate(page, limit, False).items

        # build return value
        for data in datas:
            pshare = {}
            pshare['id'] = data.Id
            pshare['name'] = data.Name
            pshare['pwd'] = data.Pwd
            pshare['nasId'] = data.NasId
            pshare['shareId'] = data.ShareId
            pshare['createTime'] = data.CreateTime.strftime('%Y-%m-%d %H:%M:%S')
            pshare['tel'] = data.Tel
            pshare['type'] = data.Type
            pshare['shareWith'] = json.loads(data.ShareWith)
            pshare['notes'] = data.Notes
            pshare['heat'] = data.HEAT
            pshare['thumbnail'] = data.Thumbnail
            RETURNVALUE[VALUE].append(pshare)

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)


def updatePShare(id):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:

        pshare = PShare.query.filter(PShare.Id == id).first()

        if pshare is None:
            RETURNVALUE[CODE] = BackendErrorCode.PSHARE_NOT_EXIST_ERROR
            RETURNVALUE[MESSAGE] = BackendErrorMessage.PSHARE_NOT_EXIST_ERROR
            log.error(RETURNVALUE)
            return buildReturnValue(RETURNVALUE)

        pshare.HEAT = pshare.HEAT + 1

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)


def removePShare(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        pshares = json.loads(param["params"].replace("'", '"').replace("u", ' '))["pshares"]
        for pshare in pshares:


            if pshare.has_key('shareId'):
                shareId = pshare['shareId']
            else:
                RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
                RETURNVALUE[MESSAGE] = "shareId necessary parameters"
                log.error(RETURNVALUE)
                return buildReturnValue(RETURNVALUE)

            if pshare.has_key('nasId'):
                nasId = pshare['nasId']
            else:
                RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
                RETURNVALUE[MESSAGE] = "nasId necessary parameters"
                log.error(RETURNVALUE)
                return buildReturnValue(RETURNVALUE)

            if pshare.has_key('type'):
                typeFilter = PShare.Type == pshare['type']

            #shareWith = str(pshare['shareWith']).replace("'", '"').replace("u", ' ')

            shareIdFilter = PShare.ShareId == shareId
            nasIdFilter = PShare.NasId == nasId


            if pshare.has_key('type'):
                PShare.query.filter(shareIdFilter, nasIdFilter, typeFilter).delete()
            else:
                PShare.query.filter(shareIdFilter, nasIdFilter).delete()
            #if type == 8:
            #    PShare.query.filter(shareIdFilter, nasIdFilter, typeFilter).delete()
            #else:
            #    if shareWith == 'None':
            #        PShare.query.filter(shareIdFilter, nasIdFilter, typeFilter).delete()
            #    else:
            #        shareWithFilter = PShare.ShareWithHash == hash(str(shareWith))
            #        PShare.query.filter(shareIdFilter, nasIdFilter, typeFilter, shareWithFilter).delete()

        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)
    
    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)


def removePShareByIds(param):
    RETURNVALUE = {}
    RETURNVALUE[VALUE] = []
    RETURNVALUE[CODE] = 0
    RETURNVALUE[MESSAGE] = None
    try:
        ids = param['ids']
        idsFilter = []
        for x in ids.split(","):
            idsFilter.append(x)
        rule = or_(*[PShare.Id == w for w in idsFilter])

        PShare.query.filter(rule).delete()
        log.info(RETURNVALUE)
        return buildReturnValue(RETURNVALUE)

    except Exception as e:
        dbRollback(db)
        RETURNVALUE[CODE] = BackendErrorCode.SYSTEM_ERROR
        RETURNVALUE[MESSAGE] = BackendErrorMessage.SYSTEM_ERROR
        log.error(e.message)
        return buildReturnValue(RETURNVALUE)