import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x = input() #sys.stdin.readlineは最後が改行
x = x + "."

dot_idx = x.find(".")
x = x[:dot_idx]
ans = int(x)
print(ans)