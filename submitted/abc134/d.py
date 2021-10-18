import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

a = list( map(int, input().split()))
b=[]
c = [0]*n
ans = 0

for i in reversed(range(n)):
    if a[i] > 1:
        print(-1)
        exit()
    cnt = n // (i+1)
    tmp = 0
    for j in range(2,cnt+1):
        tmp += c[(i+1) * j-1]
    tmp2 = (tmp%2+a[i])%2
    c[i] = tmp2
    ans += tmp2
    if tmp2 == 1:
        b.append(i+1)
b.sort()
print(ans)
print(*b, sep=' ')