# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_cors import CORS

__author__ = 'xiliangma'


#  ====================================  初始化全局实例  ====================================
app = Flask(__name__)
# 跨域访问问题
CORS(app)


# rest api type
DELETE = 'DELETE'
PUT = 'PUT'
GET = 'GET'
POST = 'POST'

#  ====================================  API  ====================================
@app.route('/')
def index():
    return "Authen Platform Services v0.1"


'''
    注册
    @param
    {'number':'',
     'name':'',
     'password':'',
    }
    @returnvalue
    {'code':'',
     'message':'',
     'value':''
    }
'''
@app.route('/api/register', methods = ['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    return "注册成功"

'''
    绑定
     @param
    {'number':'',
     'name':'',
     'password':'',
     'nasid':''
    }
'''
@app.route('/api/bind', methods = ['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    return "注册成功"


'''
    认证
    @param
    {'number':'',
      'name':'',
     'password':''
     }

    @returnvalue
    {'number':'',
     'name':'',
     'password':''
     }
'''
@app.route('/api/login', methods = ['POST'])
def login():
    return "认证成功"


'''
    随机码获取
'''
@app.route('/api/randomcode', methods = ['GET'])
def get_random_code():

    return "认证成功"


'''
    密码修改
    {'number':'',
     'name':'',
     'password':'',
     'newpassword':''
    }
'''
@app.route('/api/updatepassword', methods = ['POST'])
def update_password():
    return "认证成功"


'''
    上报pc信息
    {'number':'',
     'name':'',
     'password':'',
     'pcid':''
    }
'''
@app.route('/api/updatepassword', methods = ['POST'])
def save_pc_information():
    return "认证成功"






#  ====================================  start Flask Service  ====================================
if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)



