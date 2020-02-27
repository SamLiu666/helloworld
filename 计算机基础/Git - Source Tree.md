Git - Source Tree 操作省略代码的命令，更加方便简介，连接其中的分布式控制系统思想

[Git介绍](https://github.com/Snailclimb/JavaGuide/blob/master/docs/tools/Git.md#获取-git-仓库) [Git教程](https://www.w3cschool.cn/git/git-workspace-index-repo.html) [Source Tree 简介使用](https://www.jianshu.com/p/3cd97d0d545e) 版本控制：除了项目源代码，修改和记录一个或若干文件的变化内容，方便查找修改问题 分类：本地版本控制系统、集中化版本控制系统(CVCS)、分布式版本控制系统（DVCS) Git 仓库(.git directoty)：工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库 工作目录(Working Directory)：就是你在电脑里能看到的目录。 暂存区域(Staging Area)：英文叫stage, 或index。一般存放在"git目录"下的index文件（.git/index）中，所以我们把暂存区有时也叫作索引（index）。

“”git status 以查看在你上次提交之后是否有修改。

我演示该命令的时候加了 -s 参数，以获得简短的结果输出。如果没加该参数会详细输出内容：“”“

git config --global [user.name](http://user.name) 'SamLiu666' git config --global user.email [aa2083683710@gmail.com](http://mailto:aa2083683710@gmail.com)

```shell
liu@LAPTOP-KNM96SDR MINGW64 ~ (master)
$ cd d:  # 进入d盘

liu@LAPTOP-KNM96SDR MINGW64 /d
$ mkdir zz  #创建文件名为zz的文件

liu@LAPTOP-KNM96SDR MINGW64 /d
$ cd zz  #进入zz文件夹

liu@LAPTOP-KNM96SDR MINGW64 /d/zz
$ git init  #初始化目录，建仓完毕
Initialized empty Git repository in D:/zz/.git/

liu@LAPTOP-KNM96SDR MINGW64 /d/zz (master)
$ ls -a  # 查看仓库内文件
./  ../  .git/
```

克隆

```shell
liu@LAPTOP-KNM96SDR MINGW64 /d/zz (master)
$ git clone #克隆github上的仓库 https://github.com/SamLiu666/helloworld 

$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```