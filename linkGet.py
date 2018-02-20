# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:08:56 2018

@author: 歪克士
这是获取某首歌曲的歌词下载链接的文件
传入歌曲的ID，返回下载地址
成功返回地址，失败则返回None
"""
import urllib as ul
import re
from bs4 import BeautifulSoup as bs

def lrcGet(songPage):
    page='http://music.baidu.com/song/'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'Host':'music.baidu.com'}
    getCode=ul.request.Request(page+str(songPage),headers=headers)
    getCode=ul.request.urlopen(getCode)
    get=getCode.read()
    get=get.decode('utf-8')
    soup=bs(get,'lxml')
    aBq=soup.find_all('a','down-lrc-btn')#取class为‘down-lrc-btn’的a标签                                                                                                                                                                                                                                  
    if len(aBq)!=0:
        linkGet=str(aBq[0])
        reQ='''href":'''
        reH='''}'''
        cut=re.findall(reQ+'(.+?)'+reH,linkGet)#正则截取下载地址
        cutt=cut[0]
        cuttt=eval(cutt)#删除两侧双引号（英）
        #print(soup)
    else:
        cuttt=None
    return cuttt