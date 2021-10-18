import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

q, h,s,d, = map(int, input().split())

n = int(input())
ans = 0

qqqq = q*4
hh = h*2

best1 = min(qqqq,hh,s)

if n ==1:
    print(best1)
    exit()

if d >= best1*2:
    print(n*best1)
    exit()


else:
    d_ = n//2
    n -= d_*2
    ans += d*d_
    ans += n*best1
    print(ans)