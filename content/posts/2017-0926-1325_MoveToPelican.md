+++
title = "转移到 pelican-bootstrap3"
date = '2017-09-26 13:25:38'
aliases = [ "articles/zhuan-yi-dao-pelican-bootstrap3.html" ]

[taxonomies]
categories = ["articles"]
tags = [ "Python", " Pelican", " 博客" ]
+++

# 安装
```sh
pip install pelican markdown
```

### 解析md必须要python的markdown库, 否则不会识别md文件(又不报错).
```sh
D/c/bg pelican
WARNING: No valid files found in content.
Done: Processed 0 articles, 0 drafts, 0 pages and 0 hidden pages in 0.05 seconds.
```

## 快速开始  
新建目录用于放置站点文件,终端进入前面创建的目录运行`pelican-quickstart`后按提示操作, 那些配置也可以不管,后期再改配置文件.

## 安装主题与插件
```sh
git clone https://github.com/getpelican/pelican-themes.git   # 主题
git clone git://github.com/getpelican/pelican-plugins.git    # 插件
```
## 修改配置文件(`pelicanconf.py`)
```py
# 添加这些

# 主题路径
THEME = "pelican-themes/pelican-bootstrap3"
# 上面那个主题的需要.
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

#插件路径,启用的插件
PLUGIN_PATHS = ['pelican-plugins'] 
PLUGINS = ['i18n_subsites']
```
## 生成html

```markdown
Title: My First Review
Date: 2010-12-03 10:20
Category: Review

Following is a review of my favorite mechanical keyboard.
```
把上面的保存到 `content/MyFistReview.md`, 再运行 `pelican` 就会在 `output`文件夹生成html等.  
现在就可以启动个http服务器, 就能在 http://127.0.0.1:8080/ 看到博客了.

比如Py3自带的, 注意一定要以`output`为根目录, 否则js, css等资源加载不到, 就是html元素堆成一团浆糊.

```sh
 D/c/bg cd output/
 D/c/b/output python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 ...
```
## Pelican所需的信息

如下按顺序为标题, 创建日期, 修改日期, 分类, 标签, 链接, 作者, 摘要, 其中标题,日期不可缺.  

Status的 draft/published/hidden 可以控制是否发布.
```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Author: Alexis Metaireau
Summary: Short version for index and feeds
Status: published
```
