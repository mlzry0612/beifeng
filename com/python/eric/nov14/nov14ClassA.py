class Person:

    def __init__(self):
        print(__name__) #类的名字
        #print(__dict__) #所有属性组成的字典
        print(__class__)#类对象的类型
        self.__eat__()

    def __eat__(self):
        print("DDDD")

    def run(self):
        self.__eat__()
        print("RUN")



p = Person()
p.run()
#p.__eat()#__eat 是内部方法外面不可兔崽子
