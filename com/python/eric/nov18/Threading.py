from time import *
import threading


def music(name, loop):
    for i in range(loop):
        print('您正在听的音乐是%s' % name)
        sleep(2)
    print(ctime())


def movie(name, loop):
    for i in range(loop):
        print('您正在看的电影是%s' % name)
        sleep(3)
    print(ctime())


if __name__ == '__main__':
    t = []
    t1 = threading.Thread(target=music, args=('香水有毒', 4))
    t2 = threading.Thread(target=movie, args=('机器总动员', 4))
    t.append(t1)
    t.append(t2)
    # 第一种方式启动线程
    t1.start()
    t2.start()
   # 阻塞线程, 直到子线程全部执行完毕, 主线程才退出
    t1.join()
    t2.join()
    print('主线程')
    # 使用第二个方法启动线程
    ##   i.start()
    # for i in t:
    #    i.join()
    # print('主线程')
