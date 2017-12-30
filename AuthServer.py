# -*- coding: utf-8 -*-

__author__ = 'xiliangma'

# from backend.restApi.Resource import app
from backend.restapi.API import app
from backend.utils.LogManager import Log

logManager = Log()
log = logManager.getLogger("UsersResourcesImpl")

if __name__ == "__main__":
    log.info("Start AuthServer")
    app.run(port=8081, host='0.0.0.0', debug=True, ssl_context='adhoc')
