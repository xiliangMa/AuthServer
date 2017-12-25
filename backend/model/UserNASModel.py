# -*- coding: utf-8 -*-
__author__ = 'xiliangma'


from FlaskManager import db


class UserNAS(db.Model):

    __tablename__ = 'UserNAS'

    id = db.Column(db.Integer, primary_key = True)
    Tel = db.Column(db.BigInteger, db.ForeignKey('Users.Tel'), index = True)
    NasId = db.Column(db.String(255), db.ForeignKey('NASDevice.NasId'), index = True)
    IsAdmin = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return self

if __name__ == "__main__":
    db.create_all()
    db.session.commit()
