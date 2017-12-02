import math

if __name__ == '__main__':
    lista = []
    ss = ('22','44','55','77')
    lista = list(ss)
    print(lista)
    index = lista.index('55')
    lista.remove('55')
    lista.insert(index, '66')
    print(tuple(lista))


    L = []
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        L.append(n)
    print(L)

    m2 = lambda x, y, z: (x - y) * z


    name = [['xxx','sfssf'],['sfasdf']]
    print(name)


    m = 'qwea awwer'
    print(m[3])
    print(m[1:3])
    print(m[::-1])

    dict1 = {}
    if not dict1:
        print("DD")

    for i in range(100000):
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i
                          + 268))

        if x ** 2 == i + 100 and y ** 2 == i + 268:
            print(i)
