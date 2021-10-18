import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
ans = 1

if a.count(0)>0:
    print(0)
    exit()

for i in range(n):
    ans *= a[i]

    if ans >10**18:
        print(-1)
        exit()


print(ans)