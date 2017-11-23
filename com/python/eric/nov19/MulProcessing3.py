import multiprocessing
import time


def func1(msg):
    print("Time is %s " % time.ctime())
    time.sleep(2)
    print(msg)
    return msg + "HIGHHEEL"


if __name__ == '__main__':
    result = []
    pool = multiprocessing.Pool(processes=5)
    for i in range(5):
        asyncResult = pool.apply_async(func=func1, args=('fff - {0}'.format(i),))
        result.append(asyncResult)

    pool.close()
    pool.join()

    for res in result:
        print(res.get())