import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
p = 998244353

ketasu = len(str(n))

ans = 0

def calc_sum_serial_num(s, e):
    return ((s + e)*(e - s + 1)) // 2 % p

for i in range(ketasu-1):
    end = (10 ** i) * 9
    ans += calc_sum_serial_num(1, end)
    ans %= p

offset = 10**(ketasu-1) - 1
ans += calc_sum_serial_num(1, n - offset)
ans %= p
print(ans)