import numpy as np

array1 = np.arange(20)
print(array1)

# [10,20)
array2 = np.arange(10, 20, 1)
print(array2)

array3 = np.arange(20, 10, -2)
print(array3)

array_one = np.array([10, 20, 30])
print(array_one)

array_three = np.array([[[10, 20, 30],
                         [11, 21, 31],
                         [12, 22, 32],
                         [13, 23, 33]],
                        [[114, 124, 1242],
                         [121, 122, 123],
                         [110, 120, 130],
                         [130, 130, 134]]])
print(array_three)

# shape  描述质， 当前数组上的数量级别
print(array_three.shape)
# size  当前数组上的个数，为 shape 的值的乘积
print("数组个数 %s" % array_three.size)
# ndim 描述质
print("描述质 %d" % array_three.ndim)

# 切片三维数组
array_two = array_three[0]
# shape  描述质， 当前数组上的数量级别
print(array_two.shape)
# size  当前数组上的个数，为 shape 的值的乘积
print("数组个数 %s" % array_two.size)
# ndim 描述质
print("描述质 %d" % array_two.ndim)

# 切片2  左闭右开的
array_two_2 = array_three[0, 1:2]
print(array_two_2)
# shape  描述质， 当前数组上的数量级别
print(array_two_2.shape)
# size  当前数组上的个数，为 shape 的值的乘积
print("array_two_2数组个数 %s" % array_two_2.size)
# ndim 描述质
print("array_two_2描述质 %d" % array_two_2.ndim)

# 切片3  左闭右开的保留维度的切片, 提取多个维度的值
test = array_three[:, 1:3, 1:3]
print(test)
print("================")

# 两支括号
zeros = np.zeros((3, 2))
print(zeros)

empty = np.empty((3, 2), dtype=float)
print(empty)

# 从0到10，取5个数，这5个数等差

linspace = np.linspace(0, 10, 5)
print(linspace)

# 从0到2 log 的 base 默认为10， log10为0到 log10为2， 求5个数， 这5个数等比
logspace = np.logspace(0, 2, 5)
print(logspace)


