#!/usr/bin/env python3
"""Factorial project"""
from setuptools import find_packages, setup

setup(
    name = 'factorial', # 项目名称
    version = '1.0',    # 发布版本
    description = "Factorial module",   # 项目描述
    long_description = "A test module for our book.",   # 项目长描述
    platforms = ["Linux"],  # 模块支持平台列表
    author="JerryJi",
    author_email="support@jerryji.com",
    url="https://www.jerryji.com",
    license = "MIT",
    packages=find_packages()   # 能在源目录下找出所有模块
    )