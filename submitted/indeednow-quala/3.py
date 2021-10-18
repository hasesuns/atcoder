import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
s = list(int(input()) for i in range(n))
q = int(input())
k = list(int(input()) for i in range(q))

s.sort(reverse=True)

cnt = 0
d = [0]*(max(max(k),n)+1)

for i in range(n):
    if s[i]!=0:
        d[i]=s[i]+1
    else:
        d[i]=0

for i in k:
    print(d[i])