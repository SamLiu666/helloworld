import tkinter as tk
from Learning_interval import Learning

"""tkinter: https://zmister.com/archives/category/guidevelop/tkinter_book/"""

def hello():
    st = Learning()
    st.start_()
    print("jellp")


if __name__ == '__main__':


    root = tk.Tk(className=" Sam's Learning Window")    # 定义一个窗体,窗口名称
    button = tk.Button(master=root, text= "开始学习")
    button.pack(padx=200, pady=50)
    button.config(command=hello)    # 将按钮和函数关联

    root.mainloop()     # 将其加入主循环