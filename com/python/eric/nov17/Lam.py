from functools import reduce

ff = range(1, 33)

i = list(map(lambda x: x * 2, ff))
w = 0
for ww in i:
    print("This is %d, the value is %s" % (w, i))
    w += 1



re = [1, 2, 3, 4, 5]
print(reduce(lambda x,y: x+y, re))
