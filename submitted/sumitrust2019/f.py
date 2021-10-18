import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

t, tt = map(int, input().split())
a, aa = map(int, input().split())
b, bb = map(int, input().split())

if a*t+aa*tt == b*t+bb*tt or a*t == b*t:
    print('infinity')
    exit()

diff1 = a*t-b*t

diff12 = a*t+aa*tt - (b*t+bb*tt)

if diff1*diff12>0:
    print(0)
    exit()

diff1 = abs(diff1)
diff12 = abs(diff12)

if diff1%diff12==0:
    print(-(-diff1//diff12)*2)
else:
    print(-(-diff1//diff12)*2-1)