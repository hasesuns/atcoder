import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x, n = map(int, input().split())
p = list( map(int, input().split()))


for i in range(x,102):
    if i not in p:
        ans = i
        break

for i in reversed(range(-1,x)):
    if i not in p:
        if ans-x>=x-i:
            ans = i
        break
print(ans)