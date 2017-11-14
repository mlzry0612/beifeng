import itertools

x = range(1, 10)
y = ['a', 'b', 'c']

com1 = itertools.combinations(x, 5)
for element in com1:
    print(element)

print("=========================")
com2 = itertools.permutations(x, 4)
for element in com2:
    print(element)

print("=========================")
com3 = itertools.product(x, y)
for element in com3:
    print(element)


print("=========================")
com4 = itertools.chain(com1, com2, com3)
for element in com4:
    print(element)