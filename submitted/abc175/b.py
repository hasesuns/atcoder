import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
import  itertools

n = int(input())
l = list( map(int, input().split()))
l.sort()

ans = 0
for v in itertools.combinations(l, 3):
    if v[0] == v[1] or v[1] == v[2]:
        continue
    elif v[2] < v[0]+v[1]: ans+=1

print(ans)