import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
from collections import defaultdict
abc = [tuple(map(int,input().split())) for i in range(n-1)]
es = [[] for i in range(n)]
for a,b,c in abc:
    a,b = a-1,b-1
    es[a].append((b,c))
    es[b].append((a,c))

q, k = map(int, input().split())
xy = [tuple(map(int,input().split())) for i in range(q)]

dist = [-1]*n

def dfs(v=0,parent=-1,d=0):
    for next_v,dd in es[v]:
        if dist[next_v] == -1:
            dist[next_v] = d + dd
            dfs(next_v,v,dist[next_v])

dist[k-1] =0
dfs(k-1,-1,0)
ans=[]
for x,y in xy:
    x,y=x-1,y-1
    ans.append(dist[x]+dist[y])

print(*ans,sep='\n')