import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = list(input())[:-1]
new_n = n[:]


for i in range(1, len(n)+1):
    if n[-i] != "0":
        break
    else:
        new_n = n[:-i]

rev_n = new_n[::-1]

if new_n == rev_n:
    print('Yes')
else:
    print('No')