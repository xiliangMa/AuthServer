# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth


from backend.utils.SysConstant import *

"""
    init flask app api
"""
app = Flask(__name__, static_url_path = '')


"""
    1. init DB
"""
URI = "mysql://%s:%s@%s/%s" % (DB_USER_NAME, DB_PWD, DB_HOST, DB_NAME)
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


"""
    2. init httpAuth
"""
httpAuth = HTTPBasicAuth()


"""
    3. fix cross domain access issue
"""
CORS(app)

"""
    init logMange
"""


if __name__ == "__main__":
    print URI

