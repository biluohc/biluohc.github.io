+++
title = "Zip明文爆破"
date = '2016-10-24 21:27:07'
aliases = [ "articles/zipming-wen-bao-po.html" ]

[taxonomies]
categories = ["articles"]
tags = [ "Rust", "zip爆破" ]
+++

## 使用 Advanced Archive/Zip Password Recovery 明文破解(Known plaintext attackf) Zip 详细过程

条件： 拥有zip包内一个或以上的文件。

下载安装Advanced Archive/Zip Password Recovery ，程序自行搜索。

使用 windows 平台的 7zip (或者其它，实测 Linux下压缩的不行，估计编码不同的原因)压缩一个已知文件为**不加密的 zip**。

U![UI-Settings](http://i.imgur.com/uy9IgZJ.png)

如图，加密的zip文件选择你要解密的目标zip，

攻击类型选择明文/plaintext（如果已知文件是二进制文件，勾选允许使用二进制文件作为明文 zip 档案文件），

明文文件路径选择 已知文件压缩的 zip 文件。

然后，点击 start/开始（如果报错程序则重新压缩打开文件）,,等待 5-10 分钟，点击 stop/停止（程序得到口令才停止，然而我们只需要文件），

![UI-Stop](http://i.imgur.com/B8OLJGe.png)

然后在其弹出窗口中，点击**确定**，，会弹出窗口保存一个 file-name_decrypted.zip（如果没有，请重来，多等待..），你选择目录保存
，保存成功后会弹出 "文档成功解密"的通知。

![UI-Succeed](http://i.imgur.com/cBcpRoa.png)  

此 file-name_decrypted.zip 是未加密的，可以直接打开，取得其中的文件。
至于 口令/密码，有了内容还要它？

速度非常快，实测两三分钟（搜索秘钥完成,进度超过0%,4710MQ）即可，比起暴力破解强到哪里去了，密码是接近20位，可惜不能用于 rar,郁。

至于原理，感兴趣的自己搜索即可。

## Update on 2022

* [https://github.com/kimci86/bkcrack](https://github.com/kimci86/bkcrack)
* [https://github.com/Aloxaf/rbkcrack](https://github.com/Aloxaf/rbkcrack)
* [https://www.aloxaf.com/2019/04/zip_plaintext_attack](https://www.aloxaf.com/2019/04/zip_plaintext_attack)

