import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
import numpy as np

a,b,h,m = map(int, input().split())

mrad = 2*np.pi/60*m
hrad = 2*np.pi/12*h + 2*np.pi/12/60*m

drad = min(abs(hrad - mrad), 2*np.pi-abs(hrad-mrad) )

tmp = a**2+b**2 - 2*a*b*np.cos(drad)

ans = np.sqrt(tmp)
print(ans)