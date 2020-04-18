# shell 操作指令

```shell
# 查看文件
[lxp0@localhost ~]$ ls
apps  Desktop    Downloads  Pictures  src        Videos
data  Documents  Music      Public    Templates
# 查看文件可读性,
[lxp0@localhost ~]$ ls -l
total 0
drwxrwxr-x. 3 lxp0 lxp0  31 Apr 17 18:21 apps
drwxrwxr-x. 4 lxp0 lxp0  31 Apr 17 18:53 data
drwxr-xr-x. 2 lxp0 lxp0   6 Apr 17 17:31 Desktop
drwxr-xr-x. 2 lxp0 lxp0   6 Apr 17 17:31 Documents
drwxr-xr-x. 2 lxp0 lxp0   6 Apr 17 17:31 Downloads
drwxr-xr-x. 2 lxp0 lxp0   6 Apr 17 17:31 Music
drwxr-xr-x. 2 lxp0 lxp0   6 Apr 17 17:31 Pictures
drwxr-xr-x. 2 lxp0 lxp0   6 Apr 17 17:31 Public
drwxrwxr-x. 4 lxp0 lxp0 119 Apr 17 18:14 src
drwxr-xr-x. 2 lxp0 lxp0   6 Apr 17 17:31 Templates
drwxr-xr-x. 2 lxp0 lxp0   6 Apr 17 17:31 Videos

```



## 常见指令

- ls: 列出目录
- cd：切换目录
- pwd：显示目前的目录
- mkdir：创建一个新的目录
- rmdir：删除一个空的目录
- cp: 复制文件或目录
- rm: 移除文件或目录
- mv: 移动文件与目录，或修改文件与目录的名称

# Linux 磁盘管理

Linux磁盘管理好坏直接关系到整个系统的性能问题。

Linux磁盘管理常用三个命令为df、du和fdisk。

- df：列出文件系统的整体磁盘使用量
- du：检查磁盘空间使用量
- fdisk：用于磁盘分区

## VIM， yum