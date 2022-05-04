import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
s = input()[:-1]

yosjisho = 0
num_same = 1
now = s[0]
for i in range(1,n):
    if now == s[i]:
        num_same += 1
    else:
        yosjisho += (num_same + 1) * num_same // 2
        num_same = 1
        now = s[i]
yosjisho += (num_same + 1) * num_same // 2

ans = (n+1) * n // 2 - yosjisho
print(ans)