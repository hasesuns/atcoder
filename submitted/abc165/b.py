import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x = int(input())

ans= 0
cnt = 100
while cnt<x:
    cnt *= 1.01
    cnt = int(cnt)
    ans+=1

print(ans)