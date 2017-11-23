class DictHomeWork(object):
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
    dict1 = {1: [1, 11, 111], 2: [2, 22, 222]}
    dict2 = {3: [3, 33, 333], 4: [4, 44, 444]}
    dicthome1 = DictHomeWork(dict1)
    getkeys = dicthome1.getkeys()
    for getkey in getkeys:
        print(getkey)

    updatedict = dicthome1.updatedict(dict2)
    for update1 in updatedict:
        print(update1)

    dicthome1.delkey(1)

    getkeys = dicthome1.getkeys()
    for getkey in getkeys:
        print(getkey)

