import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame([['a', 'b', 'c', 'd'], [1, 2, 3, 4]])
print(df)

darr = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
df2 = DataFrame(darr, index=['a', 'b', 'c'], columns=['a1', 'b1', 'c1', 'd1'])
print(df2)

dict1 = {"apart": ['101', '102', '103', '104'],
         "profit": [22, 33, 44, 56],
         "year": [2001, 2002, 2003, 2005],
         "month": 9}
df3 = DataFrame(dict1)
# 把 key 当列索引， vlaue 为列数据，
df3.index = ['a', 'b', 'c', 'd']
print(df3)

print("================read text===============")
df4 = pd.read_csv('dd.csv')
df4.index = ['a', 'b', 'c']
print(df4)

df5 = pd.read_csv('dd.csv', header=None, sep=",")
df5.index = ['a', 'b', 'c', 'd']
print(df5)

print("================Data Fram nan===============")
dicta = {"apart": ['101', '102', '103', '104'],
         "profit": [22, np.nan, 44, 56],
         "year": [2001, 2002, np.nan, 2005],
         "month": 9}

dfnan1 = DataFrame(dicta)
print(dfnan1)

# 有一个 nan 就丢， 默认是行
print(dfnan1.dropna())
# 全部是 nan 才丢，默认是行
print(dfnan1.dropna(how='all'))
# 对列外理
print(dfnan1.dropna(axis=1))

print("================Data Fram nan 2===============")
dfnan2 = DataFrame(np.random.randn(7, 3))
print(dfnan2)
# 花式， 对于行先选，再选列
dfnan2.ix[:3, 1] = np.nan
dfnan2.ix[:2, 2] = np.nan

print(dfnan2)

print(dfnan2.fillna(0))
print(dfnan2.fillna(0))
# 按列修改
print(dfnan2.fillna({1: 0.5, 2: -1}))

print("================Data Fram 数学方法 ===============")
# 黑认都是按列来做, 只计算有意义的数据 不包含 nan 值
print(dfnan2.count())
print(dfnan2.mean())
print(dfnan2.sum())

print("================协方差和相关系数 ===============")
covdf = DataFrame({"GDP": [10, 12], "TEMP": [22, 26.2]})
print(covdf['GDP'].corr(covdf['TEMP']))
print(covdf['GDP'].cov(covdf['TEMP']))

print("================多重索引 ===============")
mulindex = DataFrame({'year': [2001, 2002, 2001, 2002, 2003],
                      'fruit': ['apple', 'bana', 'apple', 'bana', 'apple'],
                      'quant': [23423, 234, 123, 235, 436],
                      'prof': [222, 23526, 346, 346, 234]})
print(mulindex)

mulindex = mulindex.set_index(['fruit', 'year'])
print(mulindex.ix['apple', 2001])
print(mulindex.sum(level=['year']))
print(mulindex.mean(level=['year']))
print(mulindex.min(level=['fruit', 'year']))
