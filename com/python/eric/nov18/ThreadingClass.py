import threading


class MulthraedTest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.message = name

    def run(self):
        print("SSSS")
        print(self.message)

if __name__ == '__main__':
    for i in range(4):

        thread = MulthraedTest('wofuck-{0}'.format(i))
        thread.name='multhread-{0}'.format(i)
        thread.start()
        thread.join()
        print(thread.name)

    print("DDDD")
