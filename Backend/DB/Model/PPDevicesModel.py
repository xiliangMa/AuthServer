# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from Backend.DB.DBConn import db


class PPDevices(db.Model):

    __tablename__ = 'PPDevices'

    PPDeviceID = db.Column(db.Integer, primary_key = True, index = True)
    IsUsed = db.Column(db.BigInteger)


    def __repr__(self):
        return self

if __name__ == "__main__":
    db.create_all()
    db.session.commit()
