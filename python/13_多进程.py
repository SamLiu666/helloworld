from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('start，number[%d].' % getpid())
    print('start downloading %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download cost %d s' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python file.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('python i.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('cost%.2f s.' % (end - start))


if __name__ == '__main__':
    main()
