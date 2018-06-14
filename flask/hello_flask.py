#!/usr/bin/env python

import flask

# create the application

APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """
    显示可在‘/’访问的index页面
    :return: 
    """
    return flask.render_template('index.html')

@APP.route('/hello/<name>/')
def hello(name):
    """
    displays the page greats who ever come to visit it.
    :param name: 
    :return: 
    """
    return flask.render_template('index.html', name=name)   # 建立name变量，通过语法{{name}}返回给页面

if __name__ == '__main__':
    APP.debug = True
    APP.run()