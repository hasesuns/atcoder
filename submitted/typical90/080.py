import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, d = map(int, input().split())
a = list(map(int, input().split()))

def count_and_x_is_zero(num:int):
    return 2**(d - bin(num).count("1"))

yojishou = 0
for choise in range(1, 1<<n):
    tmp_val = 0
    for i in range(n):
        if choise&(1<<i):
            tmp_val |= a[i]
    if (bin(choise).count("1") % 2 == 1):
        yojishou += count_and_x_is_zero(tmp_val)
    else:
        yojishou -= count_and_x_is_zero(tmp_val)

ans = 2 ** d - yojishou
print(ans)