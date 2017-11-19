import multiprocessing
import time


def write1(filename, loop, lock):
    with lock:  # 用 with lock
        print('正在写入write1')
        for i in range(loop):
            with open(filename, 'a', encoding='utf-8') as file:
                file.write('我们将要学习机器学习!\n')
                time.sleep(3)


def write2(filename, loop, lock):
    lock.acquire()  # 显示 lock acquire,  release
    print('正在写入write2')
    try:
        for i in range(loop):
            with open(filename, 'a', encoding='utf-8') as file:
                time.sleep(5)
                file.write('我们将要学习深度学习!\n')
    except:
        print("DD")
    finally:
        lock.release()


if __name__ == '__main__':
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=write1, args=('lianxi3.txt', 3, lock))
    p2 = multiprocessing.Process(target=write2, args=('lianxi3.txt', 3, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
