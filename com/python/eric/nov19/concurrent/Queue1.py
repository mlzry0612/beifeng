import multiprocessing
import time
import string


def puttest(queue1):
    for i in range(5):
        queue1.put(i)
        print("PUT the object is %d"  % i)
        time.sleep(3)


def gettest(queue1):
    for i in range(5):
        getobject = queue1.get(i)
        print(getobject)


if __name__ == '__main__':
    queue = multiprocessing.Queue(5)

    putprocess = multiprocessing.Process(target=puttest, args=(queue, ))
    getprocess = multiprocessing.Process(target=gettest, args=(queue, ))
    putprocess.start()
    getprocess.start()
