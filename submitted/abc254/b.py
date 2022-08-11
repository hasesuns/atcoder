import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

ans = list([] for _ in range(n))
ans[0] = [1]

print(1)

for i in range(1, n):
    tmp = [1]
    for j in range(1, i + 1):
        if j == i:
            tmp.append(1)
        else:
            tmp.append(ans[i-1][j-1] + ans[i-1][j])
    ans[i] = tmp
    print(*tmp)