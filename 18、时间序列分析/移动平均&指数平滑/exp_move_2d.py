# 二次指数平滑
"""
当时间序列的变动出现直线趋势时，用一次指数平滑法进行预测，仍存在明显的滞后偏差。
因此，利用滞后偏差的规律建立直线趋势模型，这就是二次指数平滑法。
"""
import numpy as np
import pandas as pd

y = np.loadtxt('Pdata18_3.txt')
n = len(y)
alpha = 0.3
yh = np.zeros(n)
s1 = np.zeros(n)
s2 = np.zeros(n)
s1[0] = y[0]
s2[0] = y[0]
for i in range(1, n):
    s1[i] = alpha * y[i] + (1 - alpha) * s1[i - 1]
    s2[i] = alpha * s1[i] + (1 - alpha) * s2[i - 1]
    yh[i] = 2 * s1[i - 1] - s2[i - 1] + alpha / (1 - alpha) * (s1[i - 1] - s2[i - 1])
at = 2 * s1[-1] - s2[-1]
bt = alpha / (1 - alpha) * (s1[-1] - s2[-1])
m = np.array([1, 2])
yh2 = at + bt * m
print("预测值为：", yh2)
d = pd.DataFrame(np.c_[s1, s2, yh])
f = pd.ExcelWriter("Pdata18_3.xlsx")
d.to_excel(f)
f.close()
