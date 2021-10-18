import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, l = map(int, input().split())


amida = [[-1 for i in range(n)] for j in range(l)]

ans = 0
for i in reversed(range(l)):
    amida[i] = input()

g = input().find('o')

now = g

for i in range(l):
    if 2 <= now:
        if amida[i][now-1]=='-':
            now-=2
            continue
    if now <= n*2-2:
        if amida[i][now+1]=='-':
            now+=2
            continue

ans = now//2+1

print(ans)