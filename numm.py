# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:27:46 2018

@author: 歪克士
"""
import urllib as ul
import re
from bs4 import BeautifulSoup as bs
"""
通过歌手首页获取此歌手有多少歌曲，
为下一步判断该歌手歌曲页数做准备,
返回一个整数 idd为歌手ID

传入歌手ID即可
"""
def numm(idd):
    userPage='http://music.baidu.com/artist/'+str(idd)
    getOld=ul.request.urlopen(userPage)
    getOld=getOld.read()
    getOld=getOld.decode('utf-8')
    getbs=bs(getOld,'lxml')
    listt=getbs.find_all('a','list')
    cutQ='''歌曲'''
    cutH='''</a>'''
    chop=str(listt[0])
    resultt=re.findall(cutQ+'(.+?)'+cutH,chop)
    allNumber=resultt[0]
    allNumber=eval(allNumber)#删除两侧括号
    count=allNumber//25+1
    return count