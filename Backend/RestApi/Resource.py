# -*- coding: utf-8 -*-
__author__ = 'xiliangma'

from flask import Flask, request
from Backend.DB.DBConn import app
import UsersResourcesImpl



#  ====================================  API  ====================================
@app.route('/authserver')
def index():
    return "Authen Platform Services v0.1"

'''
    register
    @param
    {"tel":"",
     "name":"",
     "pwd":"",
     "email":"",
     "randomCode": ""
    }

    @returnvalue
    {'code':'',
     'message':'',
     'value':''
    }
'''


@app.route('/authserver/api/user/register', methods = ['POST'])
def register():
    return UsersResourcesImpl.register(request.json)


'''
    login
    @param
    {'tel':'',
     'name':'',
     'pwd':''
     }

    @returnvalue
    {'code':'',
     'message':'',
     'value':'[{"sigKey": ""}
            ]'
    }
'''


@app.route('/authserver/api/user/login', methods = ['POST'])
def login():
    return UsersResourcesImpl.login(request.json)

'''
    updatePwd
     @param
    {'tel':'',
     'newPwd':'',
     'oldPwd':''
     }

    @returnvalue
    {'code':'',
     'message':'',
     'value':''
    }
'''
@app.route('/authserver/api/user/updatepwd', methods = ['PUT'])
def updatePwd():
    return UsersResourcesImpl.updatePwd(request.json)

'''
    updatePwd
     @param
    {'tel':''
     }

    @returnvalue
    {'code':'',
     'message':'',
     'value':'{'randomCode': 1234}'
    }
'''
@app.route('/authserver/api/user/getrandomcode', methods = ['POST'])
def getRandomCode():
    return UsersResourcesImpl.getRandomCode(request.json)




if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)



