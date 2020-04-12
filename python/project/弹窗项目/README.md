# 项目功能



**设计时间间隔，时间到播放音乐，打开网页，**

**休息后重新进入学习模式**

**窗口可视化操作**

**桌面程序化运行**
**待完成**：窗口，按钮可视化。窗口输入执行次数，确认后获取传入函数


# 设计思路

**1 将原有函数类型化**

在主程序页面修改 学习时间和休息时间

| 内容                                       |      |
| ------------------------------------------ | ---- |
| 建立学习提醒类：设置默认参数，各个功能函数 |  20200330    |
| tkinter 可视化学习窗口                     |    20200331  |
|  学习窗口类型化               |    20200401  |
|  学习窗口类型化               |    20200401  |


# 实现程序

# 可视化
## 库 Tkinter

1. 学习窗口， 学习图片
2. 学习开始按钮，提示窗口：确认是否开始执行
3. 记录学习次数
4. 提前终止按钮，点击，程序结束，运行停之
5. 获取输入学习数值
6. 。。。

## 进度

**完成**

单击按钮开始学习

图片显示  

按钮外观	

获取文本数字

确定是否播放音乐

获取 文本框中的设定每次学习时间参数

**待完成**

 程序变化为windows 程序， app 等

Q：强制中断 time.sleep()

强制中断音乐播放程序

# 程序打包成exe 可执行文件

https://blog.csdn.net/lzy98/article/details/83246281?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

| 软件        |                                      |
| ----------- | ------------------------------------ |
| py2exe      | 打包好的 exe只能在相同的系统下运行， |
| pyinstaller | import 库问题                        |
| cx_Freeze   |                                      |

```java
//https://github.com/pyinstaller/pyinstaller克隆项目pyinstaller
cd F:\pyinstaller-develop\bootloader
//build the bootloader 运行
python ./waf configure build install
//重新进入根目录
cd F:\pyinstaller-develop
//安装pyinstaller
python setup.py install
//等待安装成功
```

问题

     raise ValueError("Can't mix absolute and relative paths") from None
    ValueError: Can't mix absolute and relative paths



使用 cx_Freeze 操作

1、在项目下新建setup.py 文件

```python
from cx_Freeze import setup, Executable

setup(
    name = 'learning',
    version = '0.1',
    description = 'Parse Stuff',
    executables = [Executable('main.py')]

)
```



2、当前目录下 cmd

在要打包的文件下，加入system('pause')，防止生成的exe 文件崩溃

python setup.py build



Q：图片 音乐库需要额外导入，不然在其他电脑上会报错？

路径错误

exe 拖入 cmd 会显示报错信息