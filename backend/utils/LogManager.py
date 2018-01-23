# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

import logging
import logging.handlers
from SysConstant import LOG_FILE_NAME, LOG_UPDATE_TIME, LOG_BACKUP_COUNT, LOG_UPDATE_UNIT


class Log():
    format = "%(asctime)s  %(levelname)s [%(name)s - %(funcName)s] [Thread: %(thread)d]  [Line: %(lineno)s] - %(message)s"
    logging.basicConfig(
        level = logging.DEBUG,
        format = format,
        datefmt = "%Y-%m-%d %H:%M:%S",
        filename = LOG_FILE_NAME,
        filemode = "a"
    )

    formatter = logging.Formatter(format)

    # set print format
    console = logging.StreamHandler()
    console.setFormatter(formatter)

    # 1. set log file format
    # 2. Set log save time and score
    fh = logging.handlers.TimedRotatingFileHandler(LOG_FILE_NAME, LOG_UPDATE_UNIT, LOG_UPDATE_TIME, LOG_BACKUP_COUNT, encoding='UTF-8')
    fh.setFormatter(formatter)

    def getLogger(self, name, lever = logging.INFO):
        logger = logging.getLogger(name)
        logger.setLevel(lever)

        # init log object
        logger.addHandler(self.fh)
        logger.addHandler(self.console)

        return logger

