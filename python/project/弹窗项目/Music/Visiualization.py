import tkinter as tk
from Learning_interval import Learning

"""tkinter: https://zmister.com/archives/category/guidevelop/tkinter_book/"""


class tk_window(tk.Tk):

    def __init__(self, counts):
        super(tk_window, self).__init__()
        self.counts = counts


    def window_Design(self):
        self.title("Sam' Study Window")
        self.geometry('600x500')    # 窗口大小
        # 注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
        # fm = tk.Frame(height=200, width=200, bg='green', border=2)
        # fm.pack_propagate(0)  # 固定frame大小，如果不设置，frame会随着标签大小改变
        # fm.pack()

        self.button = tk.Button(master=self, text="开始学习")
        self.button.pack(padx=200, pady=50)
        self.button.config(command=self.control)  # 将按钮和函数关联

        # self.button2 = tk.Button(master=self, text="学习次数")
        # self.button2.pack(padx=200, pady=50)
        self.button2 = tk.Button(self, text="Quit", command=self.destroy).pack()
        self.entry = tk.Entry()
        btn_set_counts= self.entry.get()    # 获取输入文本的值
        self.entry.pack()
        self.mainloop()  # 将其加入主循环

    def control(self):
        st = Learning(counts=self.counts)  # 变为False试试
        st.start_()



if __name__ == '__main__':
    #
    # app = tk_window(2)  # 设定初始学习次数
    t= tk_window(2)
    t.mainloop()
