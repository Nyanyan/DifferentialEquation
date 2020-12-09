import matplotlib.pyplot as plt
from math import exp

# 関数f(x,y)の定義
def f(idx, x, y1, y2):
    if idx == 0:
        return 8 * y1 + y2
    else:
        return 4 * y1 + 5 * y2

# 解析解
def y_analytical(idx, x):
    if idx == 0:
        return exp(4 * x) + exp(9 * x)
    else:
        return -4 * exp(4 * x) + exp(9 * x)

# 初期条件
x0 = 0
Y00 = 2
Y10 = -3

# 定数
h = 0.001
N = 200 + 1

# 解となる配列
Y = [[0 for _ in range(N)] for _ in range(2)]
x = [i * h + x0 for i in range(N)]
Y[0][0] = Y00
Y[1][0] = Y10

# オイラー法
for i in range(N - 1):
    for j in range(2):
        Y[j][i + 1] = Y[j][i] + h * f(j, x[i], Y[0][i], Y[1][i])

# 解析解
y = [[y_analytical(j, i * h + x0) for i in range(N)] for j in range(2)]

# 誤差の吟味
for i in range(2):
    error = Y[i][N - 1] - y[i][N - 1]
    # 誤差と誤差をhで割ったもの(絶対値が1に近いことが予想される)を出力
    print(error, error / h)

# グラフの表示
plt.plot(x, y[0], label="Analytical Solution of y1")
plt.plot(x, Y[0], label="Numerical Solution of y1")
plt.plot(x, y[1], label="Analytical Solution of y2")
plt.plot(x, Y[1], label="Numerical Solution of y2")
plt.legend()
plt.show()
