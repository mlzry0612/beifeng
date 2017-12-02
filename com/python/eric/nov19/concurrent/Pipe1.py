import multiprocessing


def send_data(pipe, message):
    pipe.send(message)


def recv_data(pipe):
    value = pipe.recv()
    print('接收的一个值是%s' % value)


if __name__ == '__main__':
    #Pipe里面的duplex默认的值True, 全双工管道
    pipe = multiprocessing.Pipe()
    message = 'Python'
    #  0收1发， 一定不要忘了。
    p1 = multiprocessing.Process(target=send_data, args=(pipe[1], message))
    p2 = multiprocessing.Process(target=recv_data, args=(pipe[0],))
    p1.start()
    p2.start()


#返回2个连接对象(conn1, conn2),代表管道的两端,默认是双向通信.如果duplex=False,conn1只能用来接收消息,conn2只能用来发送消息.不同于os.open之处在于os.pipe()返回2个文件描述符(r, w),表示可读的和可写的