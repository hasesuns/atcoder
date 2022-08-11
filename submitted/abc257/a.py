import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, x = map(int, input().split())

mod = -(-x // n)

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = alp[mod-1]
print(ans)