import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ans = 0
table = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        table[j] += 1
    ans += i*table[i]

print(ans)