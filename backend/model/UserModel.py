# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from sqlalchemy.sql.sqltypes import TIMESTAMP

from FlaskManager import db


class User(db.Model):

    __tablename__ = 'User'

    Tel = db.Column(db.BigInteger, primary_key = True, index = True)
    Name = db.Column(db.String(255))
    Pwd = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    SigKey = db.Column(db.Text)
    CreateTime = db.Column(TIMESTAMP)
    LastLoginTime = db.Column(TIMESTAMP)


    def __repr__(self):
        return self

if __name__ == "__main__":
    pass
    # ADD USER
    # user = User()
    # user.Tel = 15810018680
    # user.Name = 'maxl'
    # user.Pwd = hashlib.md5("abc123").hexdigest()
    # db.session.add(user)
    # db.session.commit()

    # db.create_all()
    # db.session.commit()
    # print db.session.query(User)