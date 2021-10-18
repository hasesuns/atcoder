import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, s,t = map(int, input().split())
w = int(input())
a = list(int(input()) for i in range(n-1))

ans = 0
now = w
if s<= w <= t: ans +=1
for aa in a:
    now += aa
    if s<= now <= t: ans +=1

print(ans)