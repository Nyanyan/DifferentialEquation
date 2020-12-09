import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 初期条件に使う関数
def phi(x):
    return -x * (x - 1)

# 定数
h = 0.1
k = 0.1
tn = int(1 / h) + 1
xn = int(1 / k) + 1

# 解となる配列
U = np.zeros((tn, xn))
for j in range(xn):
    #for i in range(tn):
    U[0][j] = phi(j * k)

# 陰的有限差分法(ガウス・ザイデル法を使用)
r = h / k ** 2
threshold = 1e-4
for i in range(tn - 1):
    flag = True
    while flag:
        flag = False
        pU = [j for j in U[i + 1]]
        for j in range(1, xn - 1):
            U[i + 1][j] = 1 / (1 + 2 * r) * (U[i][j] + r * U[i + 1][j - 1] + r * U[i + 1][j + 1])
            if abs(U[i + 1][j] - pU[j]) > threshold:
                flag = True

# グラフの表示
t = np.linspace(0, 1, xn)
x = np.linspace(0, 1, tn)
taxis, xaxis = np.meshgrid(t, x)
uaxis = U.reshape(taxis.shape)
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("t")
ax.set_ylabel("x")
ax.set_zlabel("u")
ax.plot_wireframe(xaxis, taxis, uaxis, color='black')
plt.show()