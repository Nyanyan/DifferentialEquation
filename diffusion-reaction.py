import cv2
import numpy as np
from random import random
from numba import jit

height = 100
width = 100
Du = 0.1
Dv = 0.05
F = 0.03
K = 0.063
U = [[1 for _ in range(width)] for _ in range(height)]
V = [[0 for _ in range(width)] for _ in range(height)]
new_U = [[0 for _ in range(width)] for _ in range(height)]
new_V = [[0 for _ in range(width)] for _ in range(height)]
img = np.zeros((height, width, 3))

radius = 5
for y in range(height):
    for x in range(width):
        y_shift = y - height // 2
        x_shift = x - width // 2
        if y_shift ** 2 + x_shift ** 2 <= radius ** 2:
            U[y][x] = 0.5
            V[y][x] = 0.5

def img_write(num):
    for y in range(height):
        for x in range(width):
            for i in range(3):
                img[y][x][i] = max(0, min(255, U[y][x] * 255))
    cv2.imwrite('img' + format(num, '0=4') + '.png',img)
    print('image', num, 'written')

loop = 10000
for i in range(loop):
    for y in range(height):
        for x in range(width):
            yu = (y - 1) % height
            yd = (y + 1) % height
            xl = (x - 1) % width
            xr = (x + 1) % width
            lu = U[yu][x] + U[yd][x] + U[y][xl] + U[y][xr] - 4 * U[y][x]
            lv = V[yu][x] + V[yd][x] + V[y][xl] + V[y][xr] - 4 * V[y][x]
            uv2 = V[y][x] ** 2 * U[y][x]
            du = Du * lu - uv2 + F * (1 - U[y][x])
            dv = Dv * lv + uv2 - (F + K) * V[y][x]
            #print(lu, lv, uv2, du, dv)
            new_U[y][x] = U[y][x] + du
            new_V[y][x] = V[y][x] + dv
    U = [[i for i in j] for j in new_U]
    V = [[i for i in j] for j in new_V]
    if i % 100 == 0:
        img_write(i // 100)
