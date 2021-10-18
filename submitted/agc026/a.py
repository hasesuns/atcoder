import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

ans = 0
cnt = 0
for i in range(1,n):
    if a[i] == a[i-1]:
        cnt +=1
    else:
        ans += -(-cnt//2)
        cnt = 0

ans += -(-cnt//2)
cnt = 0

print(ans)