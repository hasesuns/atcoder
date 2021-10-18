import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

def calc(i):
    x = a[i]-1
    cnt = 1
    while x != i:
        x = a[x]-1
        cnt+=1

    return cnt

ans = []
for i in range(n):
    ans.append(calc(i))

print(*ans,sep=' ')