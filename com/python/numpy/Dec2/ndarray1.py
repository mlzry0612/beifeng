import numpy as np

array1 = np.arange(20)
print(array1)


#[10,20)
array2 = np.arange(10, 20, 1)
print(array2)

array3 = np.arange(20, 10, -2)
print(array3)

array_one = np.array([10, 20, 30])
print(array_one)

array_two = np.array([[[10, 20, 30],
                       [10, 20, 30],
                       [10, 20, 30],
                       [10, 20, 30]],
                      [[10, 20, 30],
                       [10, 20, 30],
                       [10, 20, 30],
                       [10, 20, 30]]])
print(array_two)

# shape  描述质， 当前数组上的数量级别
print(array_two.shape)
# size  当前数组上的个数，为 shape 的值的乘积
print("数组个数 %s" % array_two.size)
# ndim 描述质
print("描述质 %d" % array_two.ndim)

# 两支括号
zeros = np.zeros((3, 2))
print(zeros)

empty = np.empty((3, 2), dtype=float)
print(empty)


#从0到10，取5个数，这5个数等差
linspace = np.linspace(0, 10, 5)
print(linspace)

#从0到2 log 的 base 默认为10， log10为0到 log10为2， 求5个数， 这5个数等比
logspace = np.logspace(0, 2, 5)
print(logspace)
