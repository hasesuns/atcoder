import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ans = (n+1)*n//2-n
print(ans)