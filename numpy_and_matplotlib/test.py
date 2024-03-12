import numpy as np
import matplotlib.pyplot as plt

# 创建一个随机数据二维数组
data = np.random.rand(100, 2)  # 生成100个随机数据的二维数组，取值范围是[0,1]

print('data: ', data)
# 将data按列进行拆分
x = data[:, 0]
y = data[:, 1]
# 绘制图形
plt.plot(x, y, 'go', markersize=5)
# 展示图形
plt.show()