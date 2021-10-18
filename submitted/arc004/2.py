import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
d = list(int(input()) for i in range(n))

ans_ma = sum(d)

print(ans_ma)

ma = max(d)
if ans_ma - ma < ma:
    print(ma - (ans_ma - ma))
else:
    print(0)