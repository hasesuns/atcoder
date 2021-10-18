import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

aa = [0, 300000, 200000, 100000]
ans=0
if n <4:
    ans += aa[n]
if m <4:
    ans += aa[m]


if n == 1 and m ==1:
    ans += 400000

print(ans)
 