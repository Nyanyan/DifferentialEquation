import matplotlib.pyplot as plt
from math import exp

# 関数f(x,y)の定義
def f(x, y):
    return x ** 2 * y ** 2 - y

# 解析解
def y_analytical(x):
    return 1 / (exp(x) + x ** 2 + 2 * x + 2)

# 初期条件
x0 = 0
Y0 = 1 / 3

# 定数
h = 0.1
N = 10 + 1

# 解となる配列
Y = [0 for _ in range(N)]
x = [i * h + x0 for i in range(N)]
Y[0] = Y0

# 修正オイラー法
for i in range(N - 1):
    x_half = x[i] + h / 2
    Y_half = Y[i] + h / 2 * f(x[i], Y[i])
    Y[i + 1] = Y[i] + h * f(x_half, Y_half)

# 解析解
y = [y_analytical(i * h + x0) for i in range(N)]

# 誤差の吟味
error = Y[N - 1] - y[N - 1]
# 誤差と誤差をh^2で割ったもの(絶対値が1に近いことが予想される)を出力
print(error, error / h ** 2)

# グラフの表示
plt.plot(x, y, label="Analytical Solution")
plt.plot(x, Y, label="Numerical Solution")
plt.legend()
plt.show()
