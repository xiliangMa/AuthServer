# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


SYSTEM_PATH = '/usr/share/AuthServer/'

# RESULT KEY
CODE = "code"
MESSAGE = "message"
VALUE = "value"

# DATA BASE
DB_USER_NAME = "authserver"
DB_PWD = "abc123"
DB_HOST = "127.0.0.1"
DB_NAME = "authserver"

# TLS
APP_ID = "1400045877"
PRIVATE_KEY = "private_key"
PUBLIC_KEY = "public_key"
tlsDir = "/backend/extend/tls_sig_api-linux-64/tools/"


# SmsSenderManager
APP_KEY = "99149c9bd054676ee989e117aecd63e6"
TEMPLATE_ID = 65720
RANDOM_CODE_TIMEOUT = 5


# requires auth
ADMIN = "admin@internal"
MD5_PWD = "e99a18c428cb38d5f260853678922e03"


# log
LOG_FILE_NAME = "/var/log/authserver/authserver.log"
LOG_PATH = "/var/log/authserver"
LOG_UPDATE_UNIT = "D"
LOG_UPDATE_TIME = 1
LOG_BACKUP_COUNT = 10


# PPD
PPD_PATH = '/usr/share/AuthServer/backend/extend/ppd_client_linux_x64/'
PPD_CLASS_PATH = PPD_PATH + 'pgJNILib.jar:' + \
                 PPD_PATH + 'pgAppLib.jar:' + \
                 PPD_PATH + 'pgWebClient.jar:' + \
                 PPD_PATH
PPD_CONFIG = PPD_PATH + 'pgTunnelSvrTool.cfg'
PPD_USER_HEAD = "__DEV_"
PPD_USER_END = "@pptun.com"
