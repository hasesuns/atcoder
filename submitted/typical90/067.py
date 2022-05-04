import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())


def base_10_to_base_n(val_base_10: int, n: int):
    if val_base_10 == 0:
        return 0
    reversed_base_n = ""
    while val_base_10:
        reversed_base_n += str(val_base_10 % n)
        val_base_10 //= n
    return int(reversed_base_n[::-1])


def base_n_to_base_10(val_base_n: int, n: int):
    val_base_10 = 0
    for c in str(val_base_n):
        val_base_10 *= n
        val_base_10 += int(c)
    return val_base_10


tmp_val = n
for i in range(k):
    val_base_10 = base_n_to_base_10(tmp_val, 8)
    val_base_9 = base_10_to_base_n(val_base_10, 9)
    tmp_val = int(str(val_base_9).replace("8", "5"))

print(tmp_val)