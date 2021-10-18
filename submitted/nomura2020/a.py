import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

h,m,hh,mm,k = map(int, input().split())

ss = h*60+m

ff = hh*60+mm

if ff-ss < 0:
    tmp = ff-ss + 24*60
else:
    tmp = ff-ss

ans = tmp - k

print(max(0,ans))