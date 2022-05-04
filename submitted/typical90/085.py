import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

k = int(input())

def divisors(n):
    ret = set()
    m = 1
    while m * m <= n:
        if n % m == 0:
            ret.add(m)
            ret.add(n // m)
        m += 1
    return ret

yakusu_list = sorted(list(divisors(k)))

ans = 0
for a in yakusu_list:
    for b in yakusu_list:
        if a * b > k:
            break
        if a > b:
            continue
        if k % (a * b) == 0 and b <= k // (a * b):
            ans += 1
print(ans)