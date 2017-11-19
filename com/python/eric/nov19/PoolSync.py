import multiprocessing
import time


def write11(filename):
    with open(filename, 'a') as write1:
        print("WRITE 1 runing time is %s" % time.ctime())
        for i in range(4):
            print("WRITE11", file=write1)  #通过 print 来自动换行
            time.sleep(4)


def write22(filename):
    with open(filename, 'a') as write2:
        print("WRITE 2 runing time is %s" % time.ctime())
        for i in range(4):
            write2.write("WRITE22")
            time.sleep(4)


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    pool.apply(func=write11, args=('pool1.txt',))
    pool.apply(func=write22, args=('pool1.txt',))
    pool.close()
    #join 阻塞主进程, 一定要在 close, terminate 之后调用
    pool.join()