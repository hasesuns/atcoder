import sys

import numpy as np

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

t = int(input())
l, x, y = map(int, input().split())
q = int(input())
e = list(int(input()) for _ in range(q))

for i in range(q):
    w = 2 * np.pi / t
    h = l / 2 * np.sin(w * e[i] - np.pi / 2) + l / 2
    y_e = - l / 2 * np.cos(w * e[i] - np.pi / 2)
    d = ((y-y_e)**2 + x**2)**0.5
    ans = np.rad2deg(np.arctan2(h, d)) 
    print(ans)
    