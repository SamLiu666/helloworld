import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
from Learning_interval import Learning

class Learning_Window(tk.Tk):

    def __init__(self):
        super(Learning_Window, self).__init__()
        self.create_window()
        self.mainloop()

   # 1. 窗口外观尺寸设计
    def create_window(self):
        # r.geometry('600x600')
        self.title("Study window")
        # 加载图片
        im = Image.open(r"D:\东蒙 人工智能课程\cs learning git\python\Project\弹窗项目\test.jpg")
        img = ImageTk.PhotoImage(im)
        self.imLabel = tk.Label(self, image=img)
        self.imLabel.pack()

    # 2. 窗口 实现功能： 单击开始学习，获取学习次数，提前结束学习，记录学习次数

    # 3. 窗口 按钮设计

    # 4.细化功能



if __name__ == '__main__':
    win = Learning_Window()