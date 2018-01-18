# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


import jpype, time
from SysConstant import PPD_CLASS_PATH, PPD_CONFIG

jvmArg = '-Djava.class.path=' + PPD_CLASS_PATH
jvmPath = jpype.getDefaultJVMPath()


class JpypeManager():

    def startJPype(self):
        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, jvmArg)


    def closeJPype(self):
        jpype.shutdownJVM()


class PPDClientManager():

    def loginPPDClient(self):
        JDClass = jpype.JClass('com.peergine.tool.pgTunnelSvrTool')
        oTool = JDClass()
        oTool.Run(PPD_CONFIG)
        return oTool


if __name__ == "__main__":
    try:
        pass
        # ppdManager = PPDServiceManager()
        # ppdManager.getPPDClient()
        # ppdManager.loginPPDClient()
        # time.sleep(3)
        # ppdManager.ppdUserList()
    except Exception as e:
        print e.message