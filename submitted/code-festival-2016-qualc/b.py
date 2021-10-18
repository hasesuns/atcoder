import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

k, t = map(int, input().split())
a = list( map(int, input().split()))


most = max(a)
hasami = k-most

print(max(0,most-hasami-1))
 