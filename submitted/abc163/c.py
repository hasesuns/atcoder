import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
ans= [0]*n

for i in range(n-1):
    ans[a[i]-1] +=1

print(*ans,sep='\n')