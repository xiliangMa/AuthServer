# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from AuthServer import oTool

class PPDClientApiManager:

    """
        isOnline 1 all 0 online
    """
    def ppdUserList(self, limit = 10000, pos = 0, isOnline = 1):
        return oTool.UserList(limit, pos, isOnline)


    def ppdUserAdd(self, userName, pwd):
        return oTool.UserAdd(userName, pwd)


    def ppdUserDelete(self, userName):
        return oTool.UserDelete(userName)


    def ppdUserUpdatePwd(self, userName, pwd):
        return oTool.UserSetPass(userName, pwd)


    def getResult(self, iReqID):
        return oTool.GetResult(iReqID)

if __name__ == "__main__":
    try:
     pass
    except Exception as e:
        print e.message
