import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = [(aa,0) for aa in a] + [(bb,1) for bb in b]
ab.sort(key=lambda x:x[0])

now_a = - 10 **9
now_b = - 2 * 10 **9
ans = 10 ** 9
for val, label in ab:
    if label == 0:
        ans = min(ans, abs(val - now_b))
        now_a = val
    else:
        ans = min(ans, abs(val - now_a))
        now_b = val

print(ans)