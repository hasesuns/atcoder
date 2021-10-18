import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

task_list = []
ab = [tuple(map(int,input().split())) for i in range(n)]

ab = sorted(ab, key=lambda x: x[1])

time = 0
for a,b in ab:
    time += a
    if time > b:
        print('No')
        exit()

print('Yes')