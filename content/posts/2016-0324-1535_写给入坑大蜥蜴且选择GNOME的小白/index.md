+++
title = "写给入坑大蜥蜴且选择GNOME的小白"
date = '2016-03-24 15:35:07'
slug = 'xie-gei-ru-keng-da-xi-yi-qie-xuan-ze-gnomede-xiao-bai'
aliases = [ "articles/xie-gei-ru-keng-da-xi-yi-qie-xuan-ze-gnomede-xiao-bai.html" ]

[taxonomies]
categories = ["articles"]
tags = [ "openSUSE", "GNOME", "Linux" ]
+++

*作者: wspsxing @ <biluohc@outlook.com>*<br>
*原贴地址: [http://tieba.baidu.com/p/4245902487](http://tieba.baidu.com/p/4245902487)*<br>
*update_log-v1.3: 改善排版,修复细节,更多有待发现. ---2016.03.24*
由** wspsxing** 最后编辑于* 2016.03.24 *。

前言:
--

从Win 转 Linux 已经大半年,期间用过众多发行版,也感受过各种桌面环境,最终选用 **openSUSE+GNOME3**。<br>
依稀记得,刚转过来时,遇到不少坑,故写个笔记，供小白们参考。

桌面镇楼:

![](https://c3.staticflickr.com/9/8566/28027857274_188b124712_b.jpg "desktop")

ps,仅供小白参考,大神请轻喷.

这张图发上来玩玩:

![](https://c7.staticflickr.com/8/7586/28612610566_f9e4861dc8_b.jpg "desktop")

一： GNOME3 第一坑,联网。
--

当初刚从 deepin 转过来时,系统和桌面环境是什么关系都不知道。<br>
百度: openSUSE 怎么连接宽带。你可以想象这有多坑**......**<br>
方法是打开终端 输入: 

* nm-connection-editor

![](https://c1.staticflickr.com/8/7602/28027856464_966f73602e_b.jpg "desktop")

再选择添加,类型 DSL,输入帐号密码保存就好了。<br>再打开顶栏右侧那个有线设置,选择你刚刚新建的 dsl
就行了。<br>
其实不用记得全部,输入 nm 按两次 Tab 就可以自动补全(如果有多个,它会都列出来,让你手动补全)。

二:GNOME 优化工具(GNOME Tweak Tool)
--

蜥蜴的 GNOME 貌似已经预装了.<br>
打开优化工具,有许多可以设置的,如图:

![](https://c1.staticflickr.com/9/8829/28360609120_8969dc0580_b.jpg "desktop")<br>

1.打开标题栏最大化,最小化按钮。双击标题栏最大化,默认就有.
---

![](https://c1.staticflickr.com/8/7522/28612610816_a510fa95ae_b.jpg "desktop")<br>

2. GNOME Shell 扩展(GNOME Shell Extensions).
---

如图:

![](https://c3.staticflickr.com/9/8208/28027856634_5a328b1376_b.jpg "desktop")

点击下面的“**获取更多扩展**”,就可以跳转到 [GNOME Shell Extensions 官
网](https://extensions.gnome.org)<br>
打开这个网站后,火狐会给你个询问,同意就是了.

2.1 安装 Dash to dock .
----

该扩展将 Dash 移出应用程序概览,并将它转变为相当标准的停靠栏。
你可以在上面那个网站搜,也可以直接点击[它](https://extensions.gnome.org/extension/307/dash-to-dock/) ,如图：

![](https://c7.staticflickr.com/9/8837/28612611006_61be050cc6_b.jpg "desktop")


点开 **OFF** ,稍后火狐就会提示你安装个东西。你同意就好了。<br>
**(注:GNOME Shell 扩展都是这么安装的)**

Dash to dock 设置:
-----

打开优化工具--扩展,如图:

![](https://c7.staticflickr.com/9/8810/28027856734_f00eb150cb_b.jpg "desktop")<br>
![](https://c5.staticflickr.com/9/8714/28612611156_c2076d5ceb_b.jpg "desktop")<br>


2.2 个人必备的 GNOME Shell 扩展:(安装后可能需要自己设置一下)
----

* **Hide top bar ——全屏自动隐藏顶栏,缺少这个 GNOME3 没法用**
* **Clipboard Indicator —— 剪切板**
* **Media player indicator —— 显示音乐播放器的状态**
* **Battery status —— 显示电池电量的百分比**
* **Netspeed ——在顶栏上显示网速**
* **Workspace indicator —— 在顶栏显示当前示工作区的序号**
* **Activities-configurator  ——活动，顶栏颜色，透明等**
* **User themes ——启用自定义的 shell 主题**
* **Lunar Calendar ——阴历(依赖 typelib-1_0-LunarDate-2_0)**
* **Openweather ——天气**
* **System-monitor ——资源监控 (依赖 NetworkManager-devel libgtop-devel)**

**你们应该自己找扩展......**

3 字体.
---

默认字体丑爆了有木有,我的是这样的:

![](https://c6.staticflickr.com/9/8019/28028759933_3b567fbb4a_b.jpg "desktop")

字体可以去 Win 的那里拷贝(*自己找也行,注意字体是有版权的,多谢某位吧友提醒 *)一份<br>
单独放在一个文件夹里(fonts),然后sudo cp -r 连着文件夹复制到/usr/share/fonts,<br>
(**sudo cp -r xxx/fonts /usr/share/fonts **(xxx请换为路径))<br>
再 **chmod 755 -R /usr/share/fonts/fonts** , 最后依次执行:

* **sudo mkfontscale**
* **sudo mkfontdir**
* **sudo fc-cache**

然后就可以在上面那个界面选择字体了。请确保每个命令都成功,如果报错请直接 **su**.<br>
*ps*,当然,你也可以双击打开字体(文件管理器里),再安装(这有可能会显示安装失败,多试几次就好了)<br>
备注:仅支持后缀为 tff,tcc 的,fon 的不能用

4 外观
---

GNOME 3 的外观与其各部分的外观有关,而其各部分可分别设定主题:

![](https://c3.staticflickr.com/9/8847/28612611226_de50d2b399_b.jpg "desktop")

| |  |
| :--- | :--- |
|GTK+主题 | GTK+应用程序的显示样式|
| 图标主题(Icon theme) | 图标主题 |
| 光标主题(Cursor theme) | 鼠标光标的主题 |
| GNOME Shell 主题(Shell theme)   | Shell 的整体外观,如顶栏的样式等,依赖于 User Themes 扩展 |

这几种主题,都可以去 GNOME-Look.org 网站 [http://gnome-look.org](http://gnome-look.org)去搜,下载安装就可以用了。<br>
我只需安装一个图标主题 numix-icon-theme-circle ,openSUSE 官网下载 dvd <br>那里([https://software.opensuse.org/421/zh_CN](https://software.opensuse.org/421/zh_CN))搜（搜不到请减少关键字）就行
(推荐这样,最方便了。)<br>

如图,这些图标都是 numix-icon-theme-circle 的:

![](https://c3.staticflickr.com/9/8676/28612611426_0162a3ce0b_b.jpg "desktop")

另外 arc-theme 是个不错的 gtk+主题,推荐。

5 Hide top bar
---

就是前面说的那个很重要的扩展。可以隐藏顶栏,实现真正的全屏.<br>
这上面的两个开了后就可以把鼠标移到顶栏,然后鼠标中键滚动就可以切换工作区,<br>一个鼠标就可以在工作区窗口之间滚来滚去,而且只要微动作的移动鼠标,
不能更爽了。注意:下面的智能隐藏要开。

![](https://c8.staticflickr.com/9/8871/28028760223_320fcab044_b.jpg "desktop")


三 :快捷键
--

全部设置---键盘,如图

![](https://c3.staticflickr.com/9/8755/28612611506_28ee0703df_b.jpg "desktop")

它这里说了,选中某项左键单击就会等你输入按键组合。<br>
如果不想改,或是错误点击什么的(这很常见),再随便按一个键(我习惯空格)就行了,因为不支持一个键的快捷键。

我一般设置一个 Alt+d ,隐藏所有窗口--就是回到桌面的意思
<br>还可以自定义快捷键:点击+后,名称和命令大可一样,主要是命令,就是软件的名字什么的。<br>如图,我这是个打开终端的快捷键(大蜥蜴默认没有):

![](https://c5.staticflickr.com/9/8571/28612611556_1799c222de_b.jpg "desktop")

四:关于 yast 一键安装卡爆的问题
--

软件源可能会有依赖或者更新,最好不要直接下载 rpm 包。
点开那个 __1 Click Instal__ ,我这里用 *imagewriter* 作例子。<br>
打开或者保存到本地再用 gedit 或其它编辑器打开。<br>
如图:

![](https://c7.staticflickr.com/9/8605/28360609270_2d55e430ea_b.jpg "desktop")

看到软件源的链接了吧然后(**zypper 多数命令须 sudo   **,以下请自行添加)：
 
* zypper ar -f http://download.opensuse.org/distribution/leap/42.1/repo/oss/  imagewriter  添加自命名源
* zypper ref   刷新软件源，中间可能会提示你是否现任该源,信任就是了。
* zypper in imagewriter    安装软件包，提示你会安装些什么，输入y就好。

关于 zypper 的使用：终端输入 zypper 就会显示使用帮助,一般是软件名+--help或软件名+-h)
---

* zypper  ref       刷新软件源
* zypper  in  xxx   安装xxx软件
* zypper  rm  xxx   移除xxx软件，加 -u 可卸载相关依赖，但你要**看清楚有什么**,否则**桌面**都可能一起卸载了
* zypper  lr        列出软件源，后加 -u 可显示源地址，加 -e 只显示已启用软件源
* zypper  rr N      删除软件源, N 是上条命令显示的源的编号（**请明白自己删的是什么**）
* zypper  ar -f URL 添加软件源， URL 是源的网址
* zypper  mr -d  N  禁用软件源 N
* zypper  mr -e  N  启用软件源 N
* zypper  al xxx    添加锁定软件包xxx状态（版本或是否安装）因为你有时发现一更新，原来卸载的又回来了
* zypper  rl xxx    移除锁定
* zypper  up        更新软件包

五:关于解码器
--

1 折腾指南
---

若是按照 [折腾指南 https://lug.ustc.edu.cn/sites/opensuse-guide/codecs.php](https://lug.ustc.edu.cn/sites/opensuse-guide/codecs.php)<br>
(当初我就不知道它的存在)一键安装后还不能用。请尝试:

* zypper dup -r packman  前提是你已经添加 packman 源,并且源的名字叫 packman .

2 手动安装
---

* zypper ar -f http://packman.inode.at/suse/openSUSE_Leap_42.1/  packman 
* zypper ar -f http://opensuse-guide.org/repo/openSUSE_Leap_42.1/  dvd
* zypper  in libdvdcss2  flash-player  ffmpeg  lame  gstreamer-plugins-base  gstreamer-plugins-good  gstreamer-plugins-good-extra  gstreamer-plugins-bad  gstreamer-plugins-bad-orig-addon  gstreamer-plugins-ugly  gstreamer-plugins-ugly-orig-addon  gstreamer-plugins-libav  dvdauthor07 

若安装好后也不能播放视频/音频,请尝试 sudo zypper dup -r packman

六 :常用软件
--

1 列表清单
---

* axel ——多线程下载工具
* alipay ——支付宝控件
* baka-mplayer ——视频播放器
* cherytree ——笔记(树形结点,富文本)
* deadbeef/audacious ——音乐播放器
* dia —— 流程图
* fbterm ——tty 显示中文
* FireFox ——浏览器
* ffmpeg ——音频视频转格式,录屏等等,本身就是解码器
* fuse-exfat    —— exfat支持
* geany ——一个轻量的 ide
* gimp ——图片编辑
* gparted ——分区工具 gparted-lang 后面这是中文的支持,很多程序都这样(xxx-lang)
* imagewriter ——制作U盘启动盘(dd 不显示进度很烦人)
* mlocate —— 搜索文件用 **locate** 安装完后/文件变动后 **sudo updatedb**(更新数据库)
* mkvtoolnix   ——视频tool
* okular ——電子書（有一堆kde的依赖，自己取舍）
* osdlyrics ——显示歌词
* qbittorrent  ——bt下载
* redshift-gtk ——降低屏幕蓝光 
* ReText ——markdown
* spek  —— 音乐频谱
* screenfetch ——不解释
* shadowsocks-qt5
* testdisk 和 phtorec ——文件恢复（教程请搜索）
* uget —— 一个像样的下载管理
* variety ——壁纸(国产也有个爱壁纸 lovewallpaper )
* VirtualBox ——虚拟机
* wine ——运行 qq
* wps-office ——office


2 某些源里没有的软件
---

1 vivaldi浏览器
----

* zypper ar  -f https://repo.fdzh.org/vivaldi/rpm/x86_64/  vivaldi-beta
* zypper in vivaldi-beta  chromium-pepper-flash

2 chrome浏览器
----

* zypper ar -f  http://repo.fdzh.org/chrome/rpm/x86_64/  chrome
* zypper in  google-chrome-stable

删除源或软件请参考** 关于 zypper 的使用**

七 :关于内存盘与 fstab
--

如果你的 RAM 富足,内存盘会给你带来更好的体验.
内存盘可以做浏览器的缓存,存放自己的临时文件,保护硬盘等。<br>
linux 下的内存盘有三种格式:

1. ramdisk 不支持自动调整大小,貌似以淘汰。
---

2. ramfs 有缺陷,设置大小完全无效。
---

设置个大小为 1M 的分区,你可以写入几个 G 乃至比你内存更多的数据,我坚信卡不死大蜥蜴,你可以试试

* mkdir mm  挂载事先要有目录,创建
* sudo mount -t ramfs -o size=50M ramfs ./mm  其中50M是指定的大小,可改
* sudo chmod 777 ./mm    改权限,以便自己帐号可以完全控制
不想用了可以sudo umount ./mm (卸载) ,不管它也没事,内存盘关机/重启就没有了，只是目录还在，删除就好.

3. tmpfs 会把 swap 也用上,其它完胜前二者(动态,大小可指定)
---

使用方法:xxx 是目录名,你也可以输入完整路径 ./指的是当前目录

* mkdir xxx
* sudo mount -t tmpfs -o size=50M tmpfs ./xxx
* sudo chmod 777 ./xxx
卸载及删除请参考上一条

4.1 /etc/fstab
---

这是开机时管理分区挂载的配置文件,写入了你的分区信息等。<br>
上面的 tmpfs 内存盘,你总不能要用再创建一个吧(当然你也可以这么做.你可以把它写入 fstab,然后开机就能自动挂载了.)<br>
修改 /etc/fstab 时请**务必小心,错了就开机不能进入图形界面**了.<br>
不建议小白修改。。,一时激动写了出来
我曾经不小心写了个中文标点 —— 逗号 __......__

* cat /etc/fstab 可以查看它,这是只读的,不要担心。
* gedit /etc/fstab 就要小心了,如果没有修改,就不要保存。
如图,我的是这样的,一行一个分区。

![](https://c7.staticflickr.com/9/8522/28612611646_78113b4209_b.jpg "desktop")<br>
\#是注释,我注释了一个交换文件。

* 第一项 UUID 是机器码(相当于身份证号),
    * **sudo lsblk -f   查看机器码** 
使用机器码则设备路径变动也不会影响启动(前提是这个分区没有动,比如被切了一部分,或者加了一部分)
也可以写设备路径,如/dev/sda1
    * sudo fdisk -l 查看硬盘分区状况(l是小写 list,列出的意思)。
* 第二项是挂载路径,是个存在的目录。
* 第三项是挂载格式,ntfs 是只读的,ntfs-3g 是支持读写的(ntfs)。
* 第四项是挂载选项, auto 是开机自动挂载, fstab 默认就是,defaults:rw ro:read-only rw:read-write,size 是大小(一般分区不需要),中间用**英文逗号**隔开。
* 第五项为 dump 选项,设置是否让备份程序 dump 备份文件系统,0 为忽略,1 为备份。选 0    .
* 第六项为 fsck 选项,告诉 fsck 程序以什么顺序检查文件系统,0 为忽略。选 0  .<br>
注意,每两项之间都有**空格**(多几个更直观)隔开.

4.2 把 tmpfs 写入 fstab
---

1:获取FireFox的缓存路径
----

firefox 地址栏输入 **about:cache** 回车即可得,<br>如图：

![](https://c4.staticflickr.com/9/8565/28028760483_6494cc2cc6_b.jpg "desktop")

就是中间 disk -->storage disk locatin 后面的:<br>
/home/viw/.cache/mozilla/firefox/51t50ppu.default/cache2    **注意这路径重装系统就会变，所以不能直接复制窝的**<br>
注: 可以清空该目录，里面只是缓存文件

* sudo gedit /etc/fstab   用gedit打开fstab文件
然后把下面这一行写到fstab最后面，注意换成**自己的路径。**
* tmpfs /home/viw/.cache/mozilla/firefox/51t50ppu.default/cache2 tmpfs    auto,size=280M 0 0  
<br>这是一行,千万不要变成两行,size=大小自己设置,和后面那图设置成一样就行。

![](https://c1.staticflickr.com/9/8011/28612611776_6efeee210e_b.jpg "desktop")

其它浏览器也是这样,先找出缓存位置,再写入 fstab 就好
设置完后

* **sudo mount -a** 看看有无错误,如果有,请在关机之前修改好。

2 :浏览器缓存搞定,现在来设置自己用的
----

我 8g 内存,设置 6g(6144M),根据你的情况自己设置。至少保证系统运行内存 2G 到 3G(你自己的占用自己清楚,我除了虚拟机,内存很少使用上 3g)。<br>
选定路径,我选择/home/viw/Download/cache (还未创建,注意替换用户名)

* mkdir /home/viw/Download/cache      先创建文件
* sudo gedit /etc/fstab       用gedit打开fstab文件

写入一行:

* tmpfs /home/viw/Downloads/cache tmpfs auto,size=6144M 0 0 
<br>保存。
照样, **sudo mount -a** 检查 (如果有错误,它会输出,一般是那个文件夹(目录)不存在
如果比较卡,请清除/home/viw/Download/cache(你自己设置的位置)目录里的文件,注意把**.Trash-1000** 文件夹清除(这就是所谓的回收站)
如图:**显示隐藏**文件,,或者终端 ls -a/la (openSUSE 设置的 alias)

![](https://c1.staticflickr.com/9/8755/28027857424_5d2693a5d1_b.jpg "desktop")

如图： **.Trash-1000** 

![](https://c1.staticflickr.com/9/8361/28360609360_8973538385_b.jpg "desktop")

4.3 把其它分区也写入 fstab,开机自动挂载 。
---

写入 fstab 的格式和前面一样.<br>
先找到设备路径:

* sudo fdisk -l (不是 1 而是 list)  

就会显示所有分区,第一个磁盘是 sda,二是 sdb,......,依此类推;<br>
sda1 是第一个磁盘第一个分区,2,3......依此类推。也可以用 blkid + 分区路径得到 UUID(如 blkid dev/sda5)。

挂载路径挂载前要先创建,自己设置(mkdir 创建空目录)<br>
我的是 /home/viw/i 雷雨 你要换成你自己设置的/dev/sda5 要换成你自己的分区路径<br>
写入 fstab 就行：

* /dev/sdb5               /home/viw/i雷雨  ntfs-3g auto    0  0
* UUID=744676BA46767CA4   /home/viw/i雷雨  ntfs-3g auto    0  0

这两都种都是对的,选一种就行了。前面也说了,ntfs 是只读的,ntfs-3g 才是读写的。

小白建议用后面的那个磁盘管理。<br>
GNOME 的磁盘/disk 也可以做到。<br>
不过比较烦,每动一个选项就要输入一次密码.<br>
我就用它取消 Win C 盘的用户界面显示,也可以设置挂载点,启动时挂载等......<br>
如图:

![](https://c8.staticflickr.com/9/8585/28028760623_e8cf0bf35d_b.jpg "desktop")

**至此,完结撒花。**


**另外,我参考了网络上的一些博客什么的(主要是名词,概念等),在此深表谢意。**

Linux 之路上,与君共勉。
--

