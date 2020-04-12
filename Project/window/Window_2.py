import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
from Learning_interval import Learning

"""https://zhuanlan.zhihu.com/p/81429343"""

class Learning_Window(tk.Tk):

    def __init__(self, freq=1, music = False, interval=1):
        super(Learning_Window, self).__init__()
        self.freq = freq    # 默认至少设定两次学习
        self.music = music
        self.interval = interval

    def main_run(self):
        # 顺序会按程序顺序执行
        self.create_window()    # 1.创建窗口
        self.show_picture()     # 2.显示图片
        self.button_design()    # 3.学习按钮 单击启动学习
        # self.get_int()          # 4.获取学习设定次数
        self.mainloop()         # 窗口循环保持运行

    # 1. 窗口外观尺寸设计
    def create_window(self):
        self.geometry('300x600')
        self.title(" Study window ")

    # 2. 窗口 按钮设计
    def button_design(self):

        # 设定学习次数
        global design_freq
        l2 = tk.Label(self, text="请设定学习次数，学习时间（默认30分钟/次）")
        l2.pack()
        design_freq = tk.Spinbox(self, from_=1, to=12)
        design_freq.pack(padx=0, pady=10)

        #设定每次学习时间
        global design_interval
        design_interval = tk.Spinbox(self, from_=30, to=60, increment=15)
        design_interval.pack(padx=0, pady=10)
        # 设定学习时间按钮 2
        # global entry
        # entry = tk.Entry(master=self)
        # entry.pack()
        # l1 = tk.Label(self, text="请输入单词学习时间(分钟)")
        # l1.pack()
        # 音乐播放按钮 3
        self.btn3 = tk.Button(master=self, text="是否结束后播放音乐")
        self.btn3.pack(padx=30, pady=20)
        self.btn3.config(command=self.play_music)  # 不加括号，点击才运行

        self.btn2 = tk.Button(master=self, text="学习设定完成\n请点击进入狂暴学习模式", command=self.get_int).pack(padx=0, pady=20)

        # # 开始学习按钮 1
        # self.btn1 = tk.Button(master=self, text="开始学习")
        # self.btn1.pack(padx=0, pady=20)  # 放置按钮的坐标位置 (side='top')
        # self.btn1.config(command=self.start_learning)  # 不加括号，点击才运行

        # 提前结束按钮
        self.btn3 = tk.Button(master=self, text="退出", command =  self.exit_window).pack(padx=0, pady=20)

    # 4.学习主循环
    def get_int(self):
        try:
            # 获取学习次数
            self.freq = int(design_freq.get())
            self.interval = int(design_interval.get())
            print('设定学习次数为：'+str(self.freq)+ '次，', "学习时间" + str(self.interval) + "分钟/次：")
            tk.messagebox.showinfo("提示", "已确定学习: " + str(self.interval) + " 分钟/次\n" + "请点击开始学习按钮")
            self.start_learning()
        except:
            tk.messagebox.showwarning("警告", "请输入整数")

    # 3. 窗口 实现功能： 单击开始学习，获取学习次数，提前结束学习，记录学习次数
    def start_learning(self):
        learning_bool = tkinter.messagebox.askyesno('提示', '确定要开始学习吗')  # 是/否，返回值true/false
        # count = 0
        if learning_bool == True:
            s = Learning(counts=self.freq, interval=self.interval)      # 设定 学习次数，学习时长
            s.music = self.music            # 是否播放音乐 bool
            print("学习中。。。")
            s.start_()
            count = s.freq
            print("此次学习设定{}次，已完成{}次".format(self.freq,count))
        else:
            print("学习已取消")

    # 5. 窗口放入图片
    def show_picture(self):
        im = Image.open("picture/test.jpg")
        global img
        img = ImageTk.PhotoImage(im)
        imLabel = tk.Label(self, image=img).pack()  # 全局变量

    # 6、确认播放音乐
    def play_music(self):
        self.music = tkinter.messagebox.askyesno('提示', '学习结束播放音乐吗？\n 确定后点击开始学习按钮')  # 是/否，返回值true/false

    # 7、结束退出程序
    def exit_window(self):
        self.destroy()
        print("已退出学习")
