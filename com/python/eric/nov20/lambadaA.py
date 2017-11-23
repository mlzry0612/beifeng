from functools import reduce


def mul3(b):
    return b * 3


list1 = [1, 2, 3, 5, 6]

listresult1 = map(mul3, list1)
for i in listresult1:
    print(i, end=" ")
print("=================")
listresult2 = map(lambda x: x * 3, list1)
for i in listresult2:
    print(i, end=" ")
print("=================")

# Reduce  把下一个元素做累计操作
list2 = [1, 2, 3, 5, 6]
print(reduce(lambda x, y: 2*x + y, list2))
print("=================")


# filter 第一个参数判断是不是 True, 如果满足，合并到一起
list4 = range(2,40,2)
listResult4 = filter(lambda x: x > 20, list4)
for i in listResult4:
    print(i, end=' ')