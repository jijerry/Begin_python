from flask import Flask, url_for, render_template, request, make_response, redirect, abort
from werkzeug import security
app = Flask(__name__)


# route装饰器用于把一个函数绑定到一个url上
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def hello_world():
    return 'hello world!!!'

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户的名称,特定的字段作为参数人传递到函数中
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 转换器规则将变量转换为特定的数据类型
    return 'Post %d' % post_id


# 请求对象
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return  log_the_user_in(request.form['username'])
        else:
            error = 'invalid username password'
    else:
        return render_template('login.html', error=error);


# 文件上传
@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/uploads' + security(f.filename))


# 读取cookies
@app.route('/')
def index():
    username = request.cookies.get('username')      #这块使用cookies.get是为了防止字典不存在是报错keyerror，请求对象的cookies属性是一个客户端发送所有的cookies字典

# 存储cookies
def index():
    resp = make_response(render_template())
    resp.set_cookie('username', 'theusername')
    return resp

# 重定向
@app.route('/')     # 从主页/重定向到不能访问的/login页面
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

# # url_for针对特定的函数构建一个url，接受函数名作为第一个参数,以及关键字参数，关键字参数应用于url变量部分
# with app.test_request_context():
#     print(url_for('hello_world'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('show_user_profile', username='jerry'))


if __name__ == '__main__':
    app.run(debug=True)