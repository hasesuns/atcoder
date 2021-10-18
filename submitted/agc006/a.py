import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
s = input() #sys.stdin.readlineは最後が改行
t = input() #sys.stdin.readlineは最後が改行

ans = 2*n
for i in range(n):
    if s[i:n] == t[:(n-i)]:
        print(2*n-(n-i))
        exit()

print(2*n)