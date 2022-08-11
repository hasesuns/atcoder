import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

for ll in l:
    ll -= 1
    if ll < k - 1:
        if a[ll] + 1 < a[ll+1]:
            a[ll] += 1
    if ll == k - 1:
        if a[ll] < n:
            a[ll] += 1

print(*a, sep=" ")