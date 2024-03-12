import numpy as np
import matplotlib.pyplot as plt

# p = np.random.uniform(0, 255, size=10)
# print(p)
# q = np.random.uniform(0, 255, size=(5, 5))
# print(q)

p1 = np.random.rand(10000)
# 由于数据太多会导致数据无法在控制台全部显示，因此该函数可以设置边界的显示数量。当edgeitems=5000时，意味着10000个数据全部显示在控制台上。
# np.set_printoptions(edgeitems=5000, suppress=True)  # 此时数据的显示格式为科学计数法, suppress的值为True时，会显示小数格式
# print(p1)
# print(p1.shape)
# 直方图显示
plt.hist(p1, bins=20, color='g', edgecolor='k')
plt.show()