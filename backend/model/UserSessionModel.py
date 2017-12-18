# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from sqlalchemy.sql.sqltypes import TIMESTAMP

from DBConn import db


class UserSession(db.Model):

    __tablename__ = 'UserSession'

    Tel = db.Column(db.BigInteger, primary_key = True, index = True, )
    RandomCode = db.Column(db.Integer)
    CreateTime = db.Column(TIMESTAMP)


    def __repr__(self):
        return self

if __name__ == "__main__":
    pass