import numpy as np
import matplotlib.pyplot as plt

N = 10000
times = 100
z = np.zeros(N)
print(type(z))
for i in range(times):
    z += np.random.rand(N)

z /= times

plt.hist(z, bins=20, color='m', edgecolor='k')
plt.show()  # 验证中心极限定理