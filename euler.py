import matplotlib.pyplot as plt

# 関数f(x,y)の定義
def f(x, y):
    return 1 + 2 * y / x

# 解析解
def y_analytical(x):
    return x * (x - 1)

# 初期条件
x0 = 1
Y0 = 0

# 定数
h = 0.01
N = 100 + 1

# 解となる配列
Y = [0 for _ in range(N)]
x = [i * h + x0 for i in range(N)]
Y[0] = Y0

# オイラー法
for i in range(N - 1):
    Y[i + 1] = Y[i] + h * f(x[i], Y[i])

# 解析解
y = [y_analytical(i * h + x0) for i in range(N)]

# 誤差の吟味
error = Y[N - 1] - y[N - 1]
# 誤差と誤差をhで割ったもの(絶対値が1に近いことが予想される)を出力
print(error, error / h)

# グラフの表示
plt.plot(x, y, label="Analytical Solution")
plt.plot(x, Y, label="Numerical Solution")
plt.legend()
plt.show()
