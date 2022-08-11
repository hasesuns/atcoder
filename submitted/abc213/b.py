import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
aa = []
for i in range(n):
    aa.append((a[i], i+1))

aa = sorted(aa, key=lambda x: -x[0])
ans = aa[1][1]

print(ans)