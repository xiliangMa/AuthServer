# 简介
AuthServer 认证平台

# 开发环境
> 基于centos 7+
 
#### 准备工作
- 初始化数据库
```
 1. 安装 mysql：
    rpm ivh http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
    yum install mysql-server
 
2. 启动 mysql： 
    systemctl start mysqld

3. 初始化访问权限
    mysql -u root -p
    CREATE DATABASE `authserver` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'authserver'@'%' IDENTIFIED BY 'abc123';
    GRANT ALL ON authserver.* TO 'authserver'@'127.0.0.1' IDENTIFIED BY 'abc123';
    
4. 初始化数据
    use authserver；
    执行AuthServerTables.sql文件的脚本
```

- 安装依赖库
> 如果报错：（npm: relocation error: npm: symbol SSL_set_cert_cb, version libssl.so.10 not defined in file libssl.so.10 with link time reference）
  执行 yum update openssl
>
```
yum install MySQL-python.x86_64
yum install java-1.8.0-openjdk-devel java-1.8.0-openjdk
yum install python2-jpype.x86_64
yum install pyOpenSSL
yum install npm 
npm install apidoc -g
```

- 安装 python 依赖库
```
easy_install pip
pip install flask==0.12.2 
pip install flask-restful 
pip install flask_sqlalchemy
pip install flask_cors 
pip install flask_httpauth
pip install qcloudsms_py
pip install sqlalchemy
pip install pyOpenSSL
pip install gunicorn
```

- 启动服务
```aidl
python AuthServer.py
```

# 编译 rpm
```
tar -zcvf AuthServer.1.0.0.tar.gz AuthServer/*
rpmbuild -tb AuthServer.1.0.0.tar.gz
```

# 生产环境
[快速部署](https://github.com/xiliangMa/AuthServer/blob/master/doc/认证服务器集群部署.docx)
  
