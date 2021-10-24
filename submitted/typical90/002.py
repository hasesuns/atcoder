import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
if n % 2 == 1:
    exit(0)
ans_list = []

for i in range(2**n):
    cnt = 0
    ans = []
    for j in range(n):
        if (i >> j) & 1 == 0:  # j桁目 is 0?
            cnt += 1
            ans.append("(")
        else:
            cnt -= 1
            ans.append(")")
        if cnt < 0 or cnt > n //2:
            break
    else:
        if cnt == 0:
            ans_list.append("".join(ans))

ans_list.sort()
print(*ans_list, sep ="\n")