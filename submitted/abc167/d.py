import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list( map(int, input().split()))


cnt = 0
path = []
visited = [False]*n
junban = [-1]*n

now = 0
while True:

    if visited[now]:
        loopstart = now
        break
    else:
        path.append(now)
        junban[now] = cnt
        visited[now]=True
        loopend = now
        cnt+=1
        now = a[now]-1

loopsize = junban[loopend] - junban[loopstart] + 1

if k < junban[loopend]:
    print(path[k]+1)
else:
    ans = path[junban[loopstart]+ (k-junban[loopstart])%loopsize]
    print(ans+1)