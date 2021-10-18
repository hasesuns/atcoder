import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


n = int(input())
ans = 0
for i in range(1,n):
    tmp = (n-1)//i
    ans +=tmp
print(ans)