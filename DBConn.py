# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from backend.utils.SysConstant import *

URI = "mysql://%s:%s@%s/%s" % (DB_USER_NAME, DB_PWD, DB_HOST, DB_NAME)
app = Flask(__name__, static_url_path = '')
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

# 跨域访问问题
CORS(app)


if __name__ == "__main__":
    print URI

