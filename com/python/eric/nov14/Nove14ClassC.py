class Father:
    def __init__(self, i ):
        print("DS"+i)
        print("Father init")

    def teach(self):
        print("Father study")

    def teach1(self):
        print("Father study")

class Son(Father):
    def __init__(self):
        super().__init__("sfs")
        print("Son init", end=" ")#更改换行符成空格

    def teach(self):
        print("Son study")


zs = Son()
zs.teach()
zs.teach1()

