import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
abc = list(map(int, input().split()))
abc.sort()
a, b, c = abc[2], abc[1], abc[0]

ans = float("inf")
for ia in range(max(n//a+2, 10000)):
    for ib in range((n-a*ia)//b+2):
        if ia + ib >= 9999:
            break
        tmp = n - a * ia - b * ib 
        if tmp >= 0 and tmp % c == 0:
            ic = tmp // c
            ans = min(ans, ia+ib+ic)

print(ans)