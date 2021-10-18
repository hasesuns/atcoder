import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, h = map(int, input().split())

a = [0]* n
b = [0]* n
for i in range(n):
    a[i], b[i] = map(int, input().split())

amax = max(a)
ans = 0

b.sort(reverse=True)

for attack in b:

    if attack < amax: break
    h -= attack
    ans += 1
    if h <= 0:
        print(ans)
        exit()

ans += -(-h//amax)

print(ans)