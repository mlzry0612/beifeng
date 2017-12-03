import numpy as np

print("==================Boolean======================")
# boolean 只返回 True位置的数据， 不判断
A = np.random.random(32).reshape([4, 8])
print(A)
B = A < 0.5
print(B)
# 2 --》 1
print(A[A > 0.5])

names = np.array(['Eric', 'Cai', 'Tom'])
scores = np.array([[10, 11, 12, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
classes = np.array(['A', 'B', 'C', 'D'])

cai_ = names == 'Cai'
# 注意array == 一个值，返回的还是一个 array
print(names == 'Cai')
#不能使用Python 中的and or
print(classes[(classes == 'B') | (classes == 'c')])

# 用 boolean的 array 直接 mapping 去取值叫矢量值，方括号里扔进去 array 进行 true/false 匹配
print(scores[names == 'Cai'])

# reshape 降低纬度，2——》1， 方括号里扔进去 array 进行 true/false 匹配
print(scores[names == 'Cai'].reshape(-1)[classes == 'B'])

print("===================Reshape=======================")
# 通过 reshap 之后生成的新 array 是一个视图， 共用一片内存空间
scores1 = np.array([[[10, 11, 12, 14],
                     [21, 22, 23, 24],
                     [31, 32, 33, 34]],
                    [[110, 111, 112, 114],
                     [121, 122, 123, 124],
                     [131, 132, 133, 134]]])
print(scores1.shape)
print(scores1.reshape(2, 2, 2, -1))

scores2 = np.arange(0, 40, 2)

# shape 是属性一定要这样赋值
scores2.shape = (2, -1)
print(scores2)


