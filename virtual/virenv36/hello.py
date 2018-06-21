from flask import Flask, url_for, render_template
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

@app.route('/login')
def login():
    pass

# # url_for针对特定的函数构建一个url，接受函数名作为第一个参数,以及关键字参数，关键字参数应用于url变量部分
# with app.test_request_context():
#     print(url_for('hello_world'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('show_user_profile', username='jerry'))


if __name__ == '__main__':
    app.run(debug=True)