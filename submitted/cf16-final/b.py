import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())


cnt =0
i=0
while cnt<n:
    i+=1
    cnt +=i

diff = cnt -n

for num in range(1,i+1):
    if num==diff: continue
    print(num)