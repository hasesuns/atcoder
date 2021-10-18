import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

k, n = map(int, input().split())
a = list( map(int, input().split()))
a.append(a[0]+k)

max_diff = 0
for i in range(len(a)-1):
    max_diff = max(max_diff, a[i+1]-a[i])

print(k-max_diff)