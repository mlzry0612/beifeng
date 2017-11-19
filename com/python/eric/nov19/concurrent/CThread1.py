from concurrent import futures
import requests
from concurrent.futures import ThreadPoolExecutor as Pool
from concurrent.futures import as_completed


def test(num):
    import time
    return time.ctime(), num * 2


with futures.ThreadPoolExecutor(max_workers=1, thread_name_prefix='wori') as executor:
    future = executor.submit(test, 1)
    print(future.result())

data = [1, 2, 3]
with futures.ThreadPoolExecutor(max_workers=1) as executor:
    for future in executor.map(test, data):
        print(future)


URLS = ['http://qq.com', 'http://sina.com', 'http://www.baidu.com', ]


def task(url, timeout=10):
    return requests.get(url, timeout=timeout)


with Pool(max_workers=3) as executor:
    future_tasks = [executor.submit(task, url) for url in URLS]

    for f in future_tasks:
        if f.running():
            print('%s is running' % str(f))

    for f in as_completed(future_tasks):
        try:
            ret = f.done()
            if ret:
                f_ret = f.result()
                print('%s, done, result: %s, %s' % (str(f), f_ret.url, len(f_ret.content)))
        except Exception as e:
            f.cancel()
            print(str(e))
