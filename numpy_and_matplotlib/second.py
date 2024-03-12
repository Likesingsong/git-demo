import numpy as np
import matplotlib.pyplot as plt

data = 2 * np.random.rand(10000, 2) - 1
print(data)
x = data[:, 0]
y = data[:, 1]
idx = x ** 2 + y ** 2 <= 1
hole = x ** 2 + y ** 2 < 0.25
idx = np.logical_and(idx, ~hole)  # 进行逻辑与操作，将在idx范围内的和不在hole范围内的下标进行与操作

plt.plot(x[idx], y[idx], 'go', markersize=1)
plt.show()