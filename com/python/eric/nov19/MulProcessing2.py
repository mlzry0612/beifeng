import multiprocessing


class clocltest(multiprocessing.Process):
    def __init__(self, name):
        super(clocltest, self).__init__()  #super在多继承中才有区别, 两种方式都可以用
        # multiprocessing.Process.__init__(self)
        self.name = name

    def run(self):
        for i in range(4):
            print(self.name)


if __name__ == '__main__':
    c = clocltest('dddsdfsf')
    c.start()
