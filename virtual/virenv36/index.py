from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import sqlite3
DATABASE = '/tmp/flaskr.db'
DUBUG = True    # 启用或者禁用交互式调试
SECURY_KEY = 'development key'  # 保持客户端会话安全
USERNAME = 'admin'
PASSWORD = 'default'

# 创建应用
app = Flask(__name__)
app.config.from_object(__name__)    # 函数寻找给定的对象，搜寻里面定义的大写变量，如上几行
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])  # 请求时打开一个连接



# 初始化数据库
# closing: with块中保持数据库连接可用， 连接是得到一个连接对象db，它提供给我们一个数据库指针，指针上有一个执行完整脚本的方法
# open_resource： 应用对象app的该方法支持这个功能，因此可以with块中直接使用，函数从当前位置（文件夹）打开一个文件，允许读取它，这里是用它在数据库连接上执行一个脚本
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode())
        db.commit()