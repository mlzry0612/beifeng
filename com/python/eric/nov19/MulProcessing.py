import multiprocessing


def writefile(filename):
    with open(filename, 'w') as write:
        write.write("1111111111\n")
        write.write("22222222222\n")


if __name__ == '__main__':

    for i in range(5):
        process = multiprocessing.Process(target=writefile, name='mulproce-{0}'.format(i), args=('mulwrite1.txt',))
        process.start()
        process.join()
        print("Process ident is %s, pid is %s, name is %s" %(process.ident, process.pid, process.name))

    print("Main exit")
