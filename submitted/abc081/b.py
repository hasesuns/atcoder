import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

ans = 1
bi = 2**ans
while True:
    for i in range(n):
        if a[i] % bi != 0:
            print(ans-1)
            exit()
    ans +=1
    bi = 2**ans