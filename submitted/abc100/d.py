import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

e000 = [0]*n
e001 = [0]*n
e010 = [0]*n
e011 = [0]*n
e100 = [0]*n
e101 = [0]*n
e110 = [0]*n
e111 = [0]*n

for i in range(n):
    x,y,z = map(int, input().split())
    e000[i]=-x-y-z
    e001[i]=-x-y+z
    e010[i]=-x+y-z
    e011[i]=-x+y+z
    e100[i]=x-y-z
    e101[i]=x-y+z
    e110[i]=x+y-z
    e111[i]=x+y+z

if m==0:
    print(0)
    exit()

e000.sort()
e001.sort()
e010.sort()
e011.sort()
e100.sort()
e101.sort()
e110.sort()
e111.sort()

elist = [e000,e001,e010,e011,e100,e101,e110,e111]

ans = 0
for e in elist:
    ans = max(ans, sum(e[-m:]))

print(ans)

 