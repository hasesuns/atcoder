import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

from collections import Counter


class PrimeFactorizations:
    def __init__(self, limit):
        self.smallest_prime_factor_list = [i for i in range(limit+1)]
        i = 2
        while i * i <= limit:
            if self.smallest_prime_factor_list[i] == i:
                for j in range(i * i, limit + 1, i):
                    if self.smallest_prime_factor_list[j] == j:
                        self.smallest_prime_factor_list[j] = i
            i += 1

    def get_divisors(self, num: int) -> Counter:
        divisors = Counter()
        while num != 1:
            divisors[self.smallest_prime_factor_list[num]] += 1
            num //= self.smallest_prime_factor_list[num]
        return divisors


pfs = PrimeFactorizations(a[-1])
divisors = set()
for aa in a:
    for divisor in pfs.get_divisors(aa):
        divisors.add(divisor)

is_coprime_list = [1] * (m + 1)
is_coprime_list[0] = 0

for divisor in list(divisors):
    for i in range(divisor, m + 1, divisor):
        is_coprime_list[i] = 0

ans = sum(is_coprime_list)
ans_list = [idx for idx, is_coprime in enumerate(is_coprime_list) if is_coprime == 1]

print(ans)
print(*ans_list, sep= "\n")