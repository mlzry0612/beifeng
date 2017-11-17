class NameNotFound(Exception):
    def __init__(self):
        print("HAHAHAH")
    pass


def div(x, y):
    if y == 0:
        raise NameNotFound
    return x/y

try:
    div(1,0)
except NameNotFound:
    print("Zero")
    print(BaseException.args)
else:
    print("SSS")
finally:
    print("DDDD")


