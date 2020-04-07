import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
from Learning_interval import Learning

"""弹窗：
 https://blog.csdn.net/Bugest/article/details/81557112?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1"""


def hello():
    learning_bool = tkinter.messagebox.askyesno('提示', '确定要开始学习吗')#是/否，返回值true/false
    count = 0
    if learning_bool == True:
        s = Learning(counts=3)
        print("学习中。。。")
        s.start_()
        count += s.counts
        print("已学习{}次".format(count))

    else:
        print("取消学习")

r = tk.Tk()
# r.geometry('600x600')
r.title("Study window")
# 加载图片
im = Image.open(r"D:\东蒙 人工智能课程\cs learning git\python\Project\弹窗项目\picture\study.jpg")
img = ImageTk.PhotoImage(im)
imLabel=tk.Label(r,image=img).pack(padx=0, pady=10)

# 1. 单击按钮 确定是否执行学习程序
btn = tk.Button(master=r, text = "学习开始")
btn.pack(padx=0,pady=20 )         # 放置按钮的坐标位置 (side='top',
count = 0
btn.config(command=hello)       # 不加括号，点击才运行


# 获取文本框内容
def get_int():
    try:
        freq = int(entry.get())
        print(freq)
        tk.messagebox.showinfo("提示", "已确定学习: "+ str(freq) + " 次\n" + "请点击开始学习按钮")
        return freq
    except:
        tk.messagebox.showwarning("警告", "请输入整数")

entry = tk.Entry(master=r)
entry.pack()
l1 = tk.Label(r, text="学习次数")
l1.pack()
btn2 = tk.Button(master=r, text="输入学习次数", command =get_int).pack()

#

# 结束按钮
btn1 = tk.Button(master=r, text = "结束学习")
btn1.pack(padx=100,pady=50 )         # 放置按钮的坐标位置 (side='top',
# r.destroy()     # 结束敞口
btn1.config(command=r.destroy)

r.mainloop()