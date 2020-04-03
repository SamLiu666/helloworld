import time,easygui,winsound, pygame, webbrowser


class Learning:
    """学习提醒"""
    def __init__(self, interval=1, web="https://www.baidu.com/", counts=2, music=False):
        # 初始化
        self.interval = interval   # 学习时间
        self.web = web              # 开启网页
        self.counts = counts        # 学习一次循环次数，默认至少1次
        self.music = music          # 默认不播放音乐

    def start_(self):
        # 主要部分
        freq = 0
        while freq < self.counts:
            time.sleep(self.interval)        # 设定为分钟，参数不要设置和time一样
            webbrowser.open(self.web)
            # 决定是否播放音乐
            if self.music == True:
                self.play_music()
            freq += 1
            print("今日已学习 {} 次（{}分钟/次）".format(freq, self.interval))

    # 播放音乐，两首歌
    def play_music(self):
        j=0
        pygame.mixer.init()
        # 设置 要播放音乐的绝对路径
        music1 = "D:\东蒙 人工智能课程\cs learning git\python\Project\弹窗项目\Music\句号.mp3"
        music2 = "D:\东蒙 人工智能课程\cs learning git\python\Project\弹窗项目\Music\那女孩对我说.mp3.mp3"
        if(j==0):
            pygame.mixer.music.load(music1)
        else:
            pygame.mixer.music.load(music2)
        while True:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play()
        j =1 if j==0 else 0

    def Horn_to_remind(self):
        # 学习时间到，鸣笛，弹窗，休息之后关闭，重新循环
        duration = 600  # millisecond
        freq = 440  # Hz
        winsound.Beep(freq, duration)

    def Visualization(self):
        easygui.msgbox("任务结束！", title="时间到！", ok_button="已休息好")

