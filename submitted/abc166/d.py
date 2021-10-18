import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x = int(input())

m = 500
aa = [0]*(m*2)
for i in range(-m,m):
    j = -m+i
    aa[j] = i**5

for i in range(m*2):
    for j in range(m*2):
        if aa[i] - aa[j] == x:
            print(-m+i,-m+j)
            exit()