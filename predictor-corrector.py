import matplotlib.pyplot as plt

# 関数f(x,y)の定義
def f(x, y):
    return 2 + x - (2 + 1 / x) * y + 1 / x * y ** 2

# 解析解
def y_analytical(x):
    return 1 / (x + 1) + x

# 初期条件
x0 = 1
Y0 = 3 / 2

# 定数
h = 0.1
N = 1000 + 1

# 解となる配列
Y = [0 for _ in range(N)]
x = [i * h + x0 for i in range(N)]
Y[0] = Y0

# 予測子修正子法
inf = 2e9
threshold = 1e-10
for i in range(N - 1):
    pre_Y = Y[i] + h * f(x[i], Y[i])
    Y[i + 1] = pre_Y
    while abs(pre_Y - Y[i + 1]) > threshold:
        Y[i + 1] = Y[i] + h / 2 * (f(x[i], Y[i]) + f(x[i + 1], pre_Y))
        pre_Y = Y[i + 1]

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
