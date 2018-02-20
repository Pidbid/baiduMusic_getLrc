# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:11:42 2018

@author: 歪克士
"""
import requests as rq
import re
from bs4 import BeautifulSoup as bs
import time 

"""获取歌手歌曲列表，其中的userId为百度音乐歌手id,返回一个音乐list
传入一个用户的ID，和总共多少页歌曲，返回一个列表。
userID 为用户ID ber为采集多少页"""
def songList(userId,ber):
    char=[]
    chom=[]
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'Host':'music.baidu.com'}    
    for ran in range(ber):
        time.sleep(1)
        urlQ='http://music.baidu.com/data/user/getsongs?start='+str(ran*25)#通过不同api接口获取不同的json
        urlH='&ting_uid='+str(userId)
        getCode=rq.get(urlQ+urlH,headers=headers)
        get=getCode.json()
        troop=get['data']['html']
        bs2=bs(troop,'lxml')
        getSpan=bs2.find_all('span','music-icon-hook')
        spanQ='''{"id":"'''
        spanH='''","type'''
        for i in getSpan:
            cut=re.findall(spanQ+'(.+?)'+spanH,str(i))
            if len(cut)!=0:
                cut=eval(cut[0])
                char.append(cut)
        chom=chom+char
        print('第%d页采集完成'%(ran+1))
    return chom