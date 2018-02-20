# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:24:24 2018

@author: 歪克士
"""
import urllib as ul
import re
from bs4 import BeautifulSoup as bs
"""
传入歌曲ID，返回歌曲标题，以供保存
失败则返回None
"""
def title(urrl):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'Host':'music.baidu.com'}
    getCode=ul.request.Request('http://music.baidu.com/song/'+str(urrl),headers=headers)
    getCode=ul.request.urlopen(getCode)
    get=getCode.read()
    get=get.decode('utf-8')
    soup=bs(get,'lxml')
    titleGet=soup.find_all('h1','music-seo')
    tQ='''title="'''
    tH='''">'''
    title=re.findall(tQ+'(.+?)'+tH,str(titleGet[0]))
    if len(title)!=0:
        title=title[0]
        title=title.strip("'")
        if '&amp;' in title:
            title=title.replace('&amp;','')
    else:
        title=None
    return title
