import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
user_dict = defaultdict(lambda: -1)
ans = []
for i in range(n):
    s = input()[:-1]
    if user_dict[s] == -1:
        user_dict[s] = i+1
        ans.append(i+1)

print(*ans, sep="\n")