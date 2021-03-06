import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 初期条件に使う関数
def phi(x):
    return -x * (x - 1)

# 定数
h = 0.004
k = 0.1
tn = int(1 / h) + 1
xn = int(1 / k) + 1

# 解に使う配列
U = np.zeros((tn, xn))
for j in range(xn):
    U[0][j] = phi(j * k)

# 陽的有限差分法
r = h / k ** 2
for i in range(tn - 1):
    for j in range(1, xn - 1):
        U[i + 1][j] = r * U[i][j + 1] + (1 - 2 * r) * U[i][j] + r * U[i][j - 1]

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