import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

from bisect import bisect_left
from bisect import bisect_right

a, b, q = map(int, input().split())

s = [0]* a
t = [0]* b
X = [0]* q
for i in range(a):
    s[i] = int(input())

for i in range(b):
    t[i] = int(input())

for i in range(q):
    X[i] = int(input())

INF = float('inf')

for x in X:
    index_ls = bisect_left(s,x)
    index_lt = bisect_left(t,x)
    index_rs = bisect_right(s,x)
    index_rt = bisect_right(t,x)
    ans = INF
    right_s = INF
    left_s = -INF
    right_t = INF
    left_t = -INF

    if index_ls < a: right_s = s[index_ls]
    if index_lt < b: right_t = t[index_lt]
    if index_rs > 0: left_s = s[index_rs-1]
    if index_rt > 0: left_t = t[index_rt-1]

    ans1 = max(right_s-x,right_t-x)
    ans2 = max(x-left_s,x-left_t)
    ans3 = right_s-x + right_s-left_t
    ans4 = right_t-x + right_t-left_s
    ans5 = x-left_t + right_s-left_t
    ans6 = x-left_s + right_t-left_s

    print(min(ans1,ans2,ans3,ans4,ans5,ans6))
 