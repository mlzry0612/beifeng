import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Series 一维数组，并产生索引¶
arr = np.array([1, 2, 3, 4])
ser1 = Series(arr)
print(ser1.values)
print(ser1.index)
# index 还有 values 都有别名
ser1.name = 'Value Name'
ser1.index.name = 'Index name'
print(ser1)

ser1.index = ['1a', '2a', '3a', '4a']
print(ser1)
print("================Series 支持一般函数, ===============")
# 并且元素仍然保持索引
print(ser1[ser1 > 2])
print(ser1 / 3)

ser2 = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(ser2)

dict1 = {'a': 1, 'b': 2}
serdict1 = Series(dict1)
print(serdict1)

print("================自动补全================")
# series 的自动补全， 拥有相同 key 的再操作， 如果没有 key 无法对应，则返回 nan 值¶
serfix = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
serfix2 = Series([1, 2, 3], index=['a', 'b', 'f'])
print(serfix + serfix2)
serfix3 = serfix + serfix2
print(pd.isnull(serfix3))


#为什么变成数组了呢
print (np.where(pd.isnull(serfix3), -1, serfix3))

print("================去重================")
serfix_dup = Series([1, 2, 2, 4], index=['a', 'b', 'c', 'd'])
print(serfix_dup.unique())
print(serfix_dup.value_counts())
print(serfix_dup.isin([2]))


