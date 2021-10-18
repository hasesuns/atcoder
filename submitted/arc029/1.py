import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
t = list(int(input()) for i in range(n))
t.sort()

if n==1:
    print(t[0])

elif n==2:
    print(t[1])

elif n==3:
    ans0=max(t[0]+t[1],t[2])
    ans1=max(t[1]+t[2],t[0])
    ans2=max(t[2]+t[0],t[1])
    print(min(ans0,ans1,ans2))
else:
    ans0=max(t[0]+t[1],t[2]+t[3])
    ans1=max(t[1]+t[2],t[3]+t[0])
    ans2=max(t[1]+t[3],t[0]+t[2])
    ans3=max(t[0],t[1]+t[2]+t[3])
    ans4=max(t[1],t[0]+t[2]+t[3])
    ans5=max(t[2],t[1]+t[0]+t[3])
    ans6=max(t[3],t[1]+t[2]+t[0])

    print(min(ans0,ans1,ans2,ans4,ans5,ans6))