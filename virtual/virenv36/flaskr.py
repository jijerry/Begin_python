# 导入所有模块
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


# 配置文件

DATABASE = '/tmp/flaskr.db'
DUBUG = True    # 启用或者禁用交互式调试
SECURY_KEY = 'development key'  # 保持客户端会话安全
USERNAME = 'admin'
PASSWORD = 'default'

# 创建应用
app = Flask(__name__)
app.config.from_object(__name__)    # 函数寻找给定的对象，搜寻里面定义的大写变量，如上几行

# app.config.from_envvar('FLASKR_SETTINGS', slice=True)   # 从配置文件加载配置，设置一个FLASKR_SETTINGS变量来设定一个配置文件覆盖默认值，slice告诉不去关心环境变量键值是否存在

# 链接到数据库
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])  # 请求时打开一个连接


if __name__ == '__main__':
    app.run()