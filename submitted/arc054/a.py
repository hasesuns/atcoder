import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

l,x,y,s,d = map(int, input().split())
ans = float('inf')
if d-s>=0:
    tmp = (d-s)/(x+y)
    ans= min(ans,tmp)
    if y>x:
        tmp = (l-d+s)/(y-x)
        ans= min(ans,tmp)
else:
    tmp = (l-s+d)/(x+y)
    ans= min(ans,tmp)
    if y>x:
        tmp = (s-d)/(y-x)
        ans= min(ans,tmp)

print(ans)