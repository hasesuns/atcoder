import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, q = map(int, input().split())
abcd = [tuple(map(int,input().split())) for i in range(q)]

ans = 0

import itertools
for seq in itertools.combinations_with_replacement(range(1,m+1),n):
    tmp = 0
    for a,b,c,d in abcd:
        if seq[b-1] - seq[a-1] == c:
            tmp += d

    ans = max(tmp,ans)

print(ans)