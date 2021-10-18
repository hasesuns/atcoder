import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n,h,w = map(int, input().split())

a = [0]* n
b = [0]* n
for i in range(n):
    a[i], b[i] = map(int, input().split())

ans = 0
for i in range(n):
    if a[i] >= h and b[i] >= w:
        ans+=1

print(ans)