import sys
import numpy as np

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())

xc = (x0 + xh) / 2
yc = (y0 + yh) / 2
rot_rad = np.pi * 2 / n

rot_matrix = np.array([
    [np.cos(rot_rad), -np.sin(rot_rad), xc-xc*np.cos(rot_rad)+yc*np.sin(rot_rad)],
    [np.sin(rot_rad), np.cos(rot_rad), yc-xc*np.sin(rot_rad)-yc*np.cos(rot_rad),],
    [0, 0, 1]
])

p0 = np.array([x0, y0, 1]).T
p1 = np.dot(rot_matrix, p0)

ans = (p1[0], p1[1])

print(*ans)