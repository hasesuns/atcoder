import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

a_soted = sorted(a)

n_group = k
expect_set_list = list(set() for _ in range(n))
real_set_list = list(set() for _ in range(n))

if k == 1:
    print('Yes')
    exit()

for i in range(n):
    amari = i % k
    real_set_list[amari].add(a[i])
    expect_set_list[amari].add(a_soted[i])

for i in range(n_group):
    if real_set_list[i] != expect_set_list[i]:
        print('No')
        exit()

print('Yes')