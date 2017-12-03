import numpy as np

reshape = np.arange(25).reshape(5, 5)
print(reshape)
#reshape[1], reshape[0] = reshape[0], reshape[1]
#print(reshape)
print(reshape[[0,1]])
print(reshape[[2,1]])

ones__reshape = np.arange(100).reshape(10,10)
print(ones__reshape)
ones__reshape[1:9][:, 1:9] = 1
print(ones__reshape)