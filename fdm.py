import matplotlib.pyplot as plt
from math import e, exp

# 解析解
c2 = 1 / (e + 1)
c3 = e / (e + 1)
def y_analytical(x):
    return c2 * exp(-x) + c3 * exp(-3 * x) - exp(-2 * x)

# 境界条件
Y0 = 0
Y1 = 0

# 定数
h = 0.1
N = 10 + 1

# 解となる配列
Y = [0 for _ in range(N)]
x = [i * h for i in range(N)]
Y[0] = Y0
Y[N - 1] = Y1

# 有限差分法(ガウス・ザイデル法を使用)
flag = True
threshold = 1e-4
k = 1 / (3 * h ** 2 - 2)
while flag:
    flag = False
    for i in range(1, N - 1):
        pY = Y[i]
        Y[i] = k * (h ** 2 * exp(-2 * x[i]) - (2 * h + 1) * Y[i + 1] + (2 * h - 1) * Y[i - 1])
        if abs(pY - Y[i]) > threshold:
            flag = True

# 解析解
y = [y_analytical(i * h) for i in range(N)]

# グラフの表示
plt.plot(x, y, label="Analytical Solution")
plt.plot(x, Y, label="Numerical Solution")
plt.legend()
plt.show()
