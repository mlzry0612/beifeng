class Father:
    def __init__(self, i ):
        print("DS"+i)
        print("Father init")

    def teach(self):
        print("Father study")


class Son(Father):
    def __init__(self):
        super().__init__("sfs")
        print("Son init")

    def teach(self):
        print("Son study")


zs = Son()
zs.teach()

