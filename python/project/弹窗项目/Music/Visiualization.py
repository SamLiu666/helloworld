import tkinter as tk
from Learning_interval import Learning

"""tkinter: https://zmister.com/archives/category/guidevelop/tkinter_book/"""


class tk_window(tk.Tk):

    def __init__(self, counts):
        super(tk_window, self).__init__()
        self.counts = counts


    def window_Design(self):
        self.title("Sam' Study Window")
        self.button = tk.Button(master=self, text="开始学习")
        self.button.pack(padx=200, pady=50)
        self.button.config(command=self.control)  # 将按钮和函数关联

        self.entry = tk.Entry()
        self.button2 = tk.Button(master=self, text="学习次数")
        self.entry.pack()
        self.button2.pack(padx=200, pady=50)


        self.mainloop()  # 将其加入主循环

    def control(self):
        st = Learning(counts=self.counts)  # 变为False试试
        st.start_()


if __name__ == '__main__':

    app = tk_window(2)
    app.window_Design()