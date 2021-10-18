import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


n = int(input())

lms = [tuple(input().split()) for i in range(n)]
es = [[] for i in range(n*2)]
from collections import defaultdict
dic = defaultdict(list)
dic_ = defaultdict(list)
from fractions import Fraction

for l, m, s in lms:
    if l not in dic.keys():
        dic[l] = len(dic)
        dic_[dic[l]] = l
    if s not in dic.keys():
        dic[s] = len(dic)
        dic_[dic[s]] = s
    es[dic[l]].append((dic[s],int(m)))
    es[dic[s]].append((dic[l],Fraction(1,int(m))))

def dfs(v=0,d=0):
    for next_v,dd in es[v]:
        if dist[next_v] == 0:
            dist[next_v] = d*dd
            dfs(next_v,dist[next_v])

ans = 1
L=0
S=0
for i in range(len(dic)):
    dist = [0]*len(dic)
    dist[i]=1
    dfs(i,1)
    tmp_max = max(dist)

    if tmp_max > ans:
        ans = tmp_max
        L = i
        S = dist.index(ans)

print(1,dic_[L],'=',ans,dic_[S],sep='')
 