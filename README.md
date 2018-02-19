# baiduMusic_getLrc
<p>
	<img src="http://www.wicos.me/wp-content/uploads/2018/02/2018021922204471-821x640.jpg" alt="" width="821" height="640" class="aligncenter size-large wp-image-395" /> 
</p>
<p>
	<span style="font-size:18px;">最前言：我会有猫的，一定会的。——海叔</span> 
</p>
<p>
	<span style="font-size:18px;"><br />
</span> 
</p>
<p>
	<span style="font-size:18px;line-height:27px;">写在前言后面：原本准备做“中国摇滚音乐究竟在唱什么”，利用云词图分析中国目前摇滚乐所唱的内容。</span> 
</p>
<p>
	<span style="font-size:18px;line-height:27px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; 可是要想获取摇滚乐所唱内容，就必须获取摇滚乐的歌词。<br />
</span> 
</p>
<p>
	<span style="font-size:18px;line-height:27px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; 因此问题从“获取摇滚乐主要内容”变成“获取摇滚乐歌词”+“歌词分析”+“云图制作”<br />
</span> 
</p>
<p>
	<span style="font-size:18px;line-height:27px;"><br />
</span> 
</p>
<p>
	<span style="font-size:18px;line-height:27px;">所以<strong>第一步</strong>就是获取摇滚乐歌词：</span> 
</p>
<p>
	<span style="font-size:18px;line-height:27px;">&nbsp; &nbsp; 1，首先想到利用开放的歌词API来获取歌词，于是找到歌词迷提供的API（<a href="http://geci.me" target="_blank">http://geci.me</a>）</span> 
</p>
<p>
	<span style="font-size:18px;line-height:27px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;但是本人认为该API不是很方便，因为只能通过“歌曲名称”和“歌手名”来获取歌词，虽然返回为json格式，但是如果批量操作存在两个缺陷①多次请求造成接口拥堵而失败。②批量操作很繁琐 所以<span style="color:#E53333;"><strong>放弃</strong></span>使用这种方法。<br />
</span> 
</p>
<p>
	<span style="font-size:18px;line-height:27px;">&nbsp; &nbsp; 2，使用歌词网获取歌词，但苦于目前没有找到结构清晰，采集方便的歌词网。所以<span style="color:#E53333;"><strong>放弃</strong></span>这个办法。<br />
</span> 
</p>
<p>
	<span style="font-size:18px;line-height:27px;"><br />
</span> 
</p>
<p>
	<img src="http://www.wicos.me/wp-content/uploads/2018/02/2018021923110879-640x640.png" alt="" width="640" height="640" class="aligncenter size-large wp-image-396" /> 
</p>
<p>
	<span style="font-size:18px;">但是一想到我未来可爱的猫纯洁的眼神，我就告诉自己“不能放弃”</span> 
</p>
<p>
	<span style="font-size:18px;">所以有了方法<strong>③自己造“轮子” 自己动手丰衣足食&nbsp;</strong></span> 
</p>
<p>
	<span style="font-size:18px;">过程如下：</span> 
</p>
<p>
	<span style="font-size:18px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一：几经周折选择了百度音乐。优点：（1）所有歌曲都是以ID的方式来辨别，不存在转码的问题。（2）可以直接在页面抓取歌词</span> 
</p>
<p>
	<span style="font-size:18px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;二：例如陈奕迅的歌手ID为1077（别问我怎么知道，我测试的都要吐了）所以歌手的主页就是“http://music.baidu.com/artist/+ID”</span> 
</p>
<p>
	<span style="font-size:18px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; 在这个页面就可以获取歌曲了。<br />
</span> 
</p>
<p>
	<span style="font-size:18px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; 那么问题①来了：百度音乐有一个问题就是每一页只能显示25首歌曲，比如陈奕迅在百度音乐有501首歌曲，那么就需要21页来显示。但是在切换页面的时候并没有通过“普通方式”（例如：在地址栏加上“&amp;page=n”此类）而是通过get获取数据。解决办法：通过抓包得到提交地址为“http://music.baidu.com/data/user/getsongs?start=+N” 其中的N为25的倍数，如果不是25的倍数，则会显示出错。提交后返回json数据。那么问题②来了，一个页面抓取之后怎么进行第二个页面的抓取呢？不急，我们从某歌手主页可以通过正则找到他在百度音乐被收录了多少歌曲。所以实际的页数也就是N%25+1（此处%为C语法，在Python3中为//）为什么+1呢？因为第一次请求json数据为“http://music.baidu.com/data/user/getsongs?start=0” 从开始，所以务必+1。将所有的歌曲ID提取，做成一个list，返回即可。<br />
</span> 
</p>
<p>
	<span style="font-size:18px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; 三：我们得到了所有的音乐ID，那么我们只需要得到歌词下载地址即可。百度歌曲的地址为“http://music.baidu.com/song/+ID” 此处的ID我们已经提取完毕。通过对这个页面的分析，我们得出该歌曲的下载地址。万事俱备，让我们来下载吧！<br />
</span> 
</p>
<p>
	<span style="font-size:18px;"><img src="http://www.wicos.me/wp-content/uploads/2018/02/2018021923315410.jpg" alt="" width="500" height="401" class="aligncenter size-full wp-image-397" /><br />
</span> 
</p>
<p>
	<span style="font-size:18px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; 四：通过下载我们终于下载了陈奕迅将近500首的歌曲歌词了。</span> 
</p>
<p>
	<span style="font-size:18px;">海叔的小猫咪表示很开心（然而我并没有猫，这是我虚构的）</span> 
</p>
<p>
	<span style="font-size:18px;"><br />
</span> 
</p>
<br />
