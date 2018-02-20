# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:39:14 2018

@author: 歪克士
下载文件，传入两个数据，下载地址和储存文件名，保存为lrc文件
"""
import urllib as ul
def downn(url,name):
    if url==None:
        print('不提供下载')
    elif name==None:
        print('不提供下载')
    else:
        ul.request.urlretrieve(url,name+'.lrc')
        print(name+'下载完毕')

    