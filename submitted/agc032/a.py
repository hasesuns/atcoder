import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
b = list( map(int, input().split()))
ans = []

while b:
    for i in reversed(range(len(b))):
        if b[i] == i+1:

            ans.append(b.pop(i))
            break

    else:
        print(-1)
        exit()

print(*reversed(ans),sep='\n')