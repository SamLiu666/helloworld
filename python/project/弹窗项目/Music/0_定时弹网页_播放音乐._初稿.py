import time, easygui
import webbrowser
import winsound
import pygame

def Learning_time():
    i=1
    j=0
    while j<3:
        i = i+1
        #时间记录，以秒为单位，学习时间默认45分钟
        time.sleep(2)
        # 到时间了打开指定网页
        url = "https://www.bilibili.com/video/av46644313?from=search&seid=14891161536312023730"
        webbrowser.open(url)
        # 默认休息五分钟，播放音乐
        pygame.mixer.init()
        if(j==0):
            pygame.mixer.music.load("句号.mp3")
        else:
            pygame.mixer.music.load("那女孩对我说.mp3")
        #循环播放
        # while True:
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()

        time.sleep(5*60)

        # 学习时间到，鸣笛，弹窗，休息之后关闭，重新循环
        duration = 600  # millisecond
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        j = j + 1

        # 休息好了点弹窗，开启下一轮学习
        easygui.msgbox("任务结束！", title="时间到！", ok_button="已休息好")

        print(j)

Learning_time()
