import numpy as np


#shape 的前部分一定要相同
arraya = np.array([[23, 22, 44, 24], [11, 22, 33, 56], [111, 122, 313, 516],[111, 122, 313, 516]])
arrayb = np.array([[12, 23], [112, 2313],[112, 2313],[112, 2313]])

print(np.dot(arraya, arrayb))

#transpose
arrayaT = arraya.T
print(arrayaT)

arraybT = arrayb.transpose();
print(arraybT)


arrayc = np.array([2,3])
arrayd = np.array([2,6])
print(np.dot(arrayc, arrayd))