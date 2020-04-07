import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
from Learning_interval import Learning

"""https://zhuanlan.zhihu.com/p/81429343"""

class Learning_Window(tk.Tk):

    def __init__(self, freq=1):
        super(Learning_Window, self).__init__()
        self.freq = freq    # 默认两次


    def main_run(self):
        # 顺序会按程序顺序执行
        self.create_window()    # 1.创建窗口
        self.show_picture()     # 2.显示图片
        self.button_design()    # 3.学习按钮 单击启动学习
        # self.get_int()          # 4.获取学习设定次数

        self.mainloop()         # 窗口循环保持运行

   # 1. 窗口外观尺寸设计
    def create_window(self):
        self.geometry('300x500')
        self.title(" Study window ")



    # 2. 窗口 按钮设计
    def button_design(self):
        # 设定学习次数按钮2
        global entry
        entry = tk.Entry(master=self)
        entry.pack()
        l1 = tk.Label(self, text="请输入学习次数")
        l1.pack()
        self.btn2 = tk.Button(master=self, text="请确认", command=self.get_int).pack(padx=0, pady=10)

        # 学习按钮1
        self.btn1 = tk.Button(master=self, text="开始学习")
        self.btn1.pack(padx=0, pady=20)  # 放置按钮的坐标位置 (side='top',
        self.btn1.config(command=self.hello)  # 不加括号，点击才运行

        # 提前结束按钮
        self.btn3 = tk.Button(master=self, text="退出", command =  self.destroy).pack(padx=0, pady=20)


    # 3. 窗口 实现功能： 单击开始学习，获取学习次数，提前结束学习，记录学习次数
    def hello(self):
        learning_bool = tkinter.messagebox.askyesno('提示', '确定要开始学习吗')  # 是/否，返回值true/false
        count = 0
        if learning_bool == True:
            s = Learning(counts=self.freq, interval=1)      # 设定 学习次数，学习时长
            print("学习中。。。")
            s.start_()
            count = s.freq
            print("已学习{}次".format(count))

        else:
            print("取消学习")

    # 4.获取文本框内容
    def get_int(self):
        try:
            self.freq = int(entry.get())
            print("设定学习" + str(self.freq)  + "次："  )
            tk.messagebox.showinfo("提示", "已确定学习: " + str(self.freq) + " 次\n" + "请点击开始学习按钮")
            return self.freq
        except:
            tk.messagebox.showwarning("警告", "请输入整数")


    # 5. 窗口放入图片
    def show_picture(self):
        im = Image.open(r"D:\东蒙 人工智能课程\cs learning git\python\Project\弹窗项目\picture\study.jpg")
        global img
        img = ImageTk.PhotoImage(im)
        imLabel = tk.Label(self, image=img).pack()  # 全局变量


if __name__ == '__main__':
    win = Learning_Window()

    win.main_run()