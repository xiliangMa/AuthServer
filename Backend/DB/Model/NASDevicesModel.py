# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from Backend.DB.DBConn import db


class NASDevices(db.Model):

    __tablename__ = 'NASDevices'

    NasId = db.Column(db.BigInteger, primary_key = True, index = True)
    IP = db.Column(db.BigInteger)
    MAC = db.Column(db.String(255))

    def __repr__(self):
        return self

if __name__ == "__main__":
    db.create_all()
    db.session.commit()
