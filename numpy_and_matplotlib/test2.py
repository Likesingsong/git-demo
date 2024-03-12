import numpy as np
import matplotlib.pyplot as plt

data = 2 * np.random.rand(1000, 2) - 1  # 生成1000个随机数据的二维数组，取值范围是[-1,1]

# 将data进行列拆分
x = data[:, 0]
y = data[:, 1]

# 选取一个圆的范围
idx = x ** 2 + y ** 2 < 1

plt.plot(x[idx], y[idx], 'go', markersize=1)
plt.show()