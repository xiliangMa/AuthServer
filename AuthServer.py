# -*- coding: utf-8 -*-

__author__ = 'xiliangma'

from backend.restapi.API import app
from backend.utils.LogManager import Log
from backend.utils.PPDServiceManager import JpypeManager


logManager = Log()
log = logManager.getLogger("AuthServer")


jpypeManager = JpypeManager()

"""
    1. build PPD Client environment
"""
status = jpypeManager.checPPDClient()
if status == 0 :
    log.info("Check PPD Client run environment success.")
else:
    log.error("Check PPD Client run environment failed.")


"""
    2. init JpypeManager
"""
log.info("Start Jpype jvm...")
jpypeManager.startJPype()


# """
#     3. init PPDServiceManager
# """
# log.info("Start PPD Client...")
# ppdService  = PPDClientManager()
# oTool = ppdService.loginPPDClient()


if __name__ == "__main__":
    log.info("Start AuthServer...")
    app.run(port=8081, host='0.0.0.0', debug=False, ssl_context='adhoc')

