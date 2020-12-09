import matplotlib.pyplot as plt
from math import sin, cos, log

# 関数f(x,y)の定義
def f(x, y):
    return sin(x * y) * cos(y) * log(x)

# 初期条件
x0 = 1
Y0 = 1

# 定数
h = 0.001
N = 9000 + 1

# 解となる配列
Y = [0 for _ in range(N)]
x = [i * h + x0 for i in range(N)]
Y[0] = Y0

# ルンゲ・クッタ法
for i in range(N - 1):
    k1 = f(x[i], Y[i])
    k2 = f(x[i] + h / 2, Y[i] + k1 / 2)
    k3 = f(x[i] + h / 2, Y[i] + k2 / 2)
    k4 = f(x[i] + h, Y[i] + h * k3)
    Y[i + 1] = Y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

# グラフの表示
plt.plot(x, Y, label="Numerical Solution")
plt.legend()
plt.show()
