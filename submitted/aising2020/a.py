import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

l,r,d = map(int, input().split())

ll = l//d
rr = r//d

ans = rr-ll

if l%d==0:
    ans+=1


print(ans)