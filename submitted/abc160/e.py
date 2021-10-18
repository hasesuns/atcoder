import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

X,Y,A,B,C = map(int, input().split())

P = list( map(int, input().split()))
Q = list( map(int, input().split()))
R = list( map(int, input().split()))

PQ = [(p,0) for p in P] + [(q,1) for q in Q]
PQ.sort(key=lambda x:x[0])
R.sort()
x=0
y=0
z=0
ans = 0
while x+y+z < X+Y:
    if R and PQ[-1][0] < R[-1]:
        ans += R.pop()
        z+=1
    else:
        tmp, label = PQ.pop()
        if label == 0 and x < X:
            ans+=tmp
            x+=1
        elif label == 1 and y < Y:
            ans+=tmp
            y+=1

print(ans)
 