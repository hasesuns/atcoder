import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
ks = [[0]*(m+1) for _ in range(m)]
ans = 0
for i in range(m):
    ks[i] = list(map(int, input().split()))
p = list( map(int, input().split()))

ans = 0
for i in range(2**n):
    isConflict = False

    for j in range(m):
        tmp = 0
        for k in ks[j][1:]:
            k -= 1
            tmp += (i >> k)
        if tmp%2 != p[j]:
            break
    else:
        ans += 1

print(ans)