from time import *
import threading


def music(name):
    print(threading.currentThread().getName())
    print(ctime())
    for i in range(3):
        print('您正在听的音乐是%s' % name)
        sleep(2)
    print(ctime())


def movie(name, loop):
    print(ctime())
    for i in range(loop):
        print('您正在看的电影是%s' % name)
        sleep(3)
    print(ctime())


if __name__ == '__main__':
    t = []
    t1 = threading.Thread(target=music, name="musicthread", args=('香水有毒',))  # 如果只有一个值， 也一定要给一个, 要不就不是元组了
    t2 = threading.Thread(target=movie, args=('机器总动员', 4))
    t.append(t1)
    t.append(t2)
    t2.setDaemon(True) #SetDaemon 要在 start 前， daemon没结束， 主线和结束了， daemon 也会死
    t1.start()
    t2.start()
    t1.join()
    print(t1.ident)
    # 阻塞线程, 直到子线程全部执行完毕, 主线程才退出
    print('主线程')


    # 使用第二个方法启动线程
    #     for i in  t:
    #         i.start()
    #     for i in t:
    #         i.join()
    #     print('主线程')
