---

---

# 项目

根据教程，建立一个博客，实现发布文章，记录标签，日期，可以评论等功能



# 进度

| 项目进度                                                     | 日期      |
| ------------------------------------------------------------ | --------- |
| 创建djaogo项目，建立数据库，让网页结构化CSS+JS+Index         | 2020/4/13 |
| 创建博客数据库后台、开发博客文章详情页、博客适用Markdown语法，代码高亮并生成目录 | 2020/4/14 |
| 自动生成文章摘要、使用自定义模板标签，分类、归档和标签页     | 2020/4/15 |
| 微博评论功能,优化博客功能细节，提升使用体验                  | 2020/4/15 |
| Nginx+Gunicorn+Supervisor 部署 Django 博客应用 https://www.bilibili.com/video/av68020610/ | 2020/4/16 |
| vmware使用，centos 虚拟机安装，xshell 连接， 部署django环境--代码 |           |



# 代码

```python
# 创建 django 项目
django-admin startproject blogproject

# 运行本地服务，查看django
python manage.py runserver

# 创建APP应用存储博客内容
python manage.py startapp blog

# 迁移数据库内容
python manage.py makemigrations
python manage.py migrate

# 创建 admin 后台管理员账户
python manage.py createsuperuser

```



python部分设置

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', # 注册 blog 应用
]
```

```shell
# 进入权限组
su root
root@server:~# adduser yangxg
# 为新用户设置密码
# 注意在输密码的时候不会有字符显示，不要以为键盘坏了，正常输入即可
root@server:~# passwd yangxg
# 把新创建的用户加入超级权限组
root@server:~# usermod -aG wheel yangxg
# 切换到创建的新用户
root@server:~# su - yangxg
# 切换成功，@符号前面已经是新用户名而不是 root 了
yangxg@server:$
```



# 安装虚拟机，xshell连接， ssh安装

[VMware安装Centos7超详细过程（图文）](https://blog.csdn.net/babyxue/article/details/80970526?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1)

[获取root权限](https://blog.csdn.net/xy_myy/article/details/81173184?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1)

```shell
# 创建虚拟环境
virtualenv env1
# 启动虚拟环境
source bin/activate

```

# Django，Nginx和uWSGI

## Nginx

[介绍](https://zhuanlan.zhihu.com/p/34943332) [介绍](https://juejin.im/post/5e982d4b51882573b0474c07)

**定义** 轻量级的Web服务器，反向代理服务器，内存少，启动快，高并发能力强

反向代理服务器： 

**Master: 读取并验证配置文件nginx.conf；管理worker进程；**

**Worker: 每一个Worker进程都维护一个线程（避免线程切换），处理连接和请求；注意Worker进程的个数由配置文件决定，一般和CPU个数相关（有利于进程切换），配置几个就有几个Worker进程**

Django是一个开放源代码的Web应用框架，由Python写成。Django不是一个服务器，只是一个Web的应用框架。

WSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。用于连接Web服务器和Web应用框架。

![原理](https://img-blog.csdn.net/20181008155327375?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lpbG92ZXhpbmc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

[配置过程](https://blog.csdn.net/yilovexing/article/details/82969103?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2)



