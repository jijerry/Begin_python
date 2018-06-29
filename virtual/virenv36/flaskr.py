# 导入所有模块
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# 配置文件

DATABASE = '.\\tmp\\flaskr.db'
DUBUG = True    # 启用或者禁用交互式调试
SECRET_KEY = 'development key'  # 保持客户端会话安全
USERNAME = 'admin'
PASSWORD = 'default'

# 创建应用
app = Flask(__name__)
app.config.from_object(__name__)    # 函数寻找给定的对象，搜寻里面定义的大写变量，如上几行

# app.config.from_envvar('FLASKR_SETTINGS', slice=True)   # 从配置文件加载配置，设置一个FLASKR_SETTINGS变量来设定一个配置文件覆盖默认值，slice告诉不去关心环境变量键值是否存在

# 链接到数据库
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


@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
# 显示条目
def show_entires():
    cur = g.db.execute('select title, text from entires ORDER BY id DESC')     #游标返回的是声明的列组织的元组
    entires = [dict(title=row[0], text =row[1]) for row in cur.fetchall()]
    return render_template('show_entires.html', entires=entires)        #视图函数将条目作为字典传给html模板渲染并返回渲染结果

@app.route('/add', methods=['POST'])
# 登录用户添加新条目
def add_entry():
    if not session.get('logged_in'):        # 检查用户登录，logged_in存在会话中，为true
        abort(401)
    g.db.execute('insert into entires (title, text) VALUES (?, ?)', [request.form['title'], request.form['text']])      # 用？标记构建sql语句，使用格式化字符串容易遭受SQL注入
    g.db.commit()
    flash("new entry was successfully posted")      # 向下一个请求闪现一条信息然后跳转回show_entires页面
    return redirect(url_for('show_entires'))


@app.route('/login', methods=['GET', 'POST'])
# 登录
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'invalid password'
        else:
            session['logged_in'] = True
            flash('you were logged in')
            return redirect(url_for('show_entires'))
    return render_template('login.html', error=error)

@app.route('/logout')
# 注销登录
def logout():
    session.pop('logged_in', None)      # 字典中删除logged_in键值，这样不需要检查用户是否登录
    flash('you were logged out')
    return redirect(url_for('show_entires'))

if __name__ == '__main__':
    app.run()