#!/usr/bin/env python


import os
import os.path
import requests

def download(url):
    '''
    从指定的URL中下载文件并存储到当前的目录
    :param url: 要下载的文件URL
    :return: 
    '''
    req = requests.get(url)

    if req.status_code == 404:
        print('No such file found at %s' % url)
        return

    with open('sample.txt', 'wb') as fobj:

        fobj.write(req.content)
    print("download over")


if __name__ == '__main__':

    url = input('enter the url: ')
    download(url)
