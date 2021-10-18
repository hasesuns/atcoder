import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())

aa = [1]*n

for i in range(k):

    d = int(input())
    a = list( map(int, input().split()))
    for a_ in a:
        aa[a_-1]=0

print(sum(aa))