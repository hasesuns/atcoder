import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())

num_prime_factor_list = [0] * (n+1)
ans = 0

for number in range(2, n+1):
    if num_prime_factor_list[number] == 0:  # numberが素数の時
        for i_times in range(1, n//number+1):
            num_prime_factor_list[number * i_times] += 1

    if num_prime_factor_list[number] >= k:
        ans += 1

print(ans)