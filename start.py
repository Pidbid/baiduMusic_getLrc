# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:30:24 2018

@author: 歪克士
"""

import linkGet 
import numm
import titleGet
import madePage
import downn
import time

id=input('请输入歌手ID：')
pageNumber=numm.numm(id)
allId=madePage.songList(id,pageNumber)
print(allId)
for i in allId:
    down=linkGet.lrcGet(i)
    titlee=titleGet.title(i)
    downn.downn(down,titlee)
print('所有歌词下载完毕')