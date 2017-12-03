import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x ** 2)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='$sin(x)$', color='red', linewidth=3)
plt.plot(x, z, 'b--', label='$cos(x**2)$')
plt.xlabel('XXXXX')
plt.ylabel('YYYYY')
plt.ylim(-1.2, 1.2)
plt.legend(loc = 'lower right')
plt.grid(True)
plt.show()


