class ListHomeWork(object):
    def __init__(self, dict1):
        self.dict1 = dict1

    def delkey(self, key):
        # self.dict1.pop(key)
        if self.dict1.keys().__contains__(key):
            self.dict1.pop(key)
        else:
            print("This key %s not exit" % key)

    def getkeys(self):
        return list(self.dict1.keys())

    def updatedict(self, dict2):
        self.dict1.update(dict2)
        return self.dict1.values()


if __name__ == '__main__':
    a = "dsafasdf"
    try:
        a + 1
        print("SSS")
    except:
        print("DDD")


