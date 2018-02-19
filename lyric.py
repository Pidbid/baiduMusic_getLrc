# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:23:33 2018

@author: 歪克士
"""

import urllib as ul
import requests as rq
import re
from bs4 import BeautifulSoup as bs
import time 

urlTest='http://music.baidu.com/song/800733'
"""
定义获取歌词代码函数
如果成功，则返回真实下载地址
如果该歌曲没有歌词，则返回None
"""
def lrcGet(songPage):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'Host':'music.baidu.com'}
    getCode=ul.request.Request(songPage,headers=headers)
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

"""
根据歌曲地址返回歌曲名称,应该和第一个lrcGet同步
"""
def title(urrl):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'Host':'music.baidu.com'}
    getCode=ul.request.Request(urrl,headers=headers)
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
"""
通过歌手首页获取此歌手有多少歌曲，
为下一步判断该歌手歌曲页数做准备,
返回一个整数
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
    print('本次采集共%d页'%(count))
    return count

"""获取歌手歌曲列表，其中的userId为百度音乐歌手id,返回一个音乐list"""
def songList(userId,ber):
    char=[]
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'Host':'music.baidu.com'}    
    for ran in range(ber):
        time.sleep(3)
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
        print('第%d页采集完成'%(ran+1))
    return char

"""
下载歌词:(其中的dUrl为百度音乐歌手的ID，例如陈奕迅的ID为1077)
    使用多个函数返回值，
    1，文件下载地址 函数lrcGet
    2，文件名 函数title
    3，多个歌曲ID 函数 songList
"""
def down(dUrl):
    print('开始进行下载')
    listO=songList(dUrl,numm(dUrl))
    print('本次共下载%d首歌曲的歌词,请保持网络畅通，否则可能会失败。'%(len(listO)))
    pageQ='http://music.baidu.com/song/'
    for i in listO:
        downUrl=lrcGet(pageQ+str(i))
        downTitle=title(pageQ+str(i))
        print('已获取%s的下载地址，准备开始下载'%(downTitle))
        print(downUrl)
        time.sleep(3.5)
        if downUrl==None:
            print('%s不提供下载'%(downTitle))
        else:
            if downTitle==None:
                print('格式错误')
            else:
                ul.request.urlretrieve(downUrl,downTitle+'.lrc')
                print('完成')     
    print('本次下载完成')

down(1077)













                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

