# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from sqlalchemy.sql.sqltypes import TIMESTAMP
from FlaskManager import db
from NASDevicesModel import NASDevices
from UserModel import User


class PShare(db.Model):

    __tablename__ = 'PShare'

    Id = db.Column(db.Integer, primary_key = True)
    NasId = db.Column(db.BigInteger, db.ForeignKey(NASDevices.NasId))
    ShareId = db.Column(db.Integer)
    Name = db.Column(db.String(255))
    Type = db.Column(db.Integer)
    ShareWith = db.Column(db.Text)
    ShareWithHash = db.Column(db.String(255))
    Notes = db.Column(db.Text)
    Tel = db.Column(db.BigInteger, db.ForeignKey(User.Tel))
    CreateTime = db.Column(TIMESTAMP)
    HEAT = db.Column(db.Integer)

    def __repr__(self):
        return self

if __name__ == "__main__":
    db.create_all()
    db.session.commit()
