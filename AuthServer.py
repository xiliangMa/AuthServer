# -*- coding: utf-8 -*-

__author__ = 'xiliangma'

from backend.restapi.API import app
from backend.utils.LogManager import Log
from backend.utils.PPDServiceManager import PPDClientManager, JpypeManager


logManager = Log()
log = logManager.getLogger("AuthServer")


"""
init JpypeManager
"""
jpypeManager = JpypeManager()
jpypeManager.startJPype()


"""
    init PPDServiceManager
"""
ppdService  = PPDClientManager()
oTool = ppdService.loginPPDClient()


if __name__ == "__main__":
    logManager.cheLogFile()
    log.info("Start AuthServer")
    app.run(port=8081, host='0.0.0.0', debug=False, ssl_context='adhoc')

