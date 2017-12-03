import numpy as np

print("===================基本类型=======================")
# numpy 会自动判断类型,通过以下方法更改类型
e = np.array([2, 3, 4], dtype='int8')
e.astype('int8')

ar = np.array([1, 2, 3, 4, 5])
print(ar)
print(ar + 1)
print(ar * 3)
print(ar / 3)
print(ar ** 2)

print("===================dot=======================")
arrayc = np.array([[2, 3, 4], [1.1, 2.2, 3.3]])
arrayd = np.array([[2, 6, 9], [1, 2, 3], [1, 2, 3]])
#2*2+3*1+4*1
print(np.dot(arrayc, arrayd))


print("===================axis0 纵, axis1 横=======================")
print("==============一元函数======================")
arraye = np.array([[2, 3, 4], [1.1, 2.2, 3.3],
                   [10.1, 20.2, 30.3]])
print(arraye.max(axis=0))
print(arraye.min(axis=0))
print(arraye.mean(axis=0))


print("==============二元函数======================")
arrayw = np.random.random(20)
print(arrayw)
print(np.power(arrayw, 3))

print("==============聚合函数======================")
print(arraye.std(axis=1))


print("==============聚合函数-where======================")
#常用于数据清理
arr = np.array([[1,2,np.inf],
                [np.nan,3,4],
                [np.nan,2,1]])
condi = np.isnan(arr) | np.isinf(arr)
print(np.where(condi, 0, arr))

