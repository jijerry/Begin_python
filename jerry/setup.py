#!/usr/bin/env python3
"""Factorial project"""
from setuptools import find_packages, setup

setup(name = 'jerry',   # 项目名称
    version = '0.2',        # 发布版本
    description = "Factorial module.",      # 项目介绍
    long_description = "A test module for our book.",   # 项目描述
    platforms = ["Linux"],      # 项目支持平台列表
    author="Jerry",
    author_email="support@xunlei.com",
    url="https://www.xunlei.com/courses/596",
    license = "MIT",
    packages=find_packages()    # 在源代码目录找出所有模块的特殊函数
    )
