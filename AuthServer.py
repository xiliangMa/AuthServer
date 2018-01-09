# -*- coding: utf-8 -*-

__author__ = 'xiliangma'

from backend.restapi.API import app
from backend.utils.LogManager import Log
from backend.utils.BackendUtils import cheLogFile

logManager = Log()
log = logManager.getLogger("UsersResourcesImpl")

if __name__ == "__main__":
    cheLogFile()
    log.info("Start AuthServer")
    app.run(port=8081, host='0.0.0.0', debug=True, ssl_context='adhoc')
