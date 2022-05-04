import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

l, r = map(int, input().split())
p = 10 ** 9 + 7

inv2 = 2 ** (p-2) % p
def calc_lr_sum(l: int, r: int):
    return (l + r) % p * (r - l + 1) % p * inv2 % p

ans = 0
for rank in range(19):
    ll = max(l, 10**rank)
    rr = min(r, 10**(rank+1)-1)
    if ll > rr: continue
    ans += calc_lr_sum(ll, rr) * (rank+1)
    ans %= p

print(ans%p)