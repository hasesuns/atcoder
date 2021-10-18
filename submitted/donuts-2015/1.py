import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
import numpy as np

n, m = map(int, input().split())
print(n*n*np.pi*m*2*np.pi)