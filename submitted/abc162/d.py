import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
s = input() #sys.stdin.readlineは最後が改行

r = [0]*n
g = [0]*n
b = [0]*n

for i in range(n):
    if s[i] == 'R':r[i]+=1
    elif s[i] == 'G':g[i]+=1
    else: b[i]+=1

from itertools import accumulate
r_nokori = list(reversed(r))
r_nokori = list(reversed(list(accumulate(r_nokori))))
g_nokori = list(reversed(g))
g_nokori = list(reversed(list(accumulate(g_nokori))))
b_nokori = list(reversed(b))
b_nokori = list(reversed(list(accumulate(b_nokori))))

ans = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        if s[i]==s[j]: continue

        if (s[i]=='R' and s[j]=='G') or (s[i]=='G' and s[j]=='R'):
            ans += b_nokori[j+1]
            if 2*j-i <= n:
                if s[2*j-i] == 'B': ans-= 1

        if (s[i]=='G' and s[j]=='B') or (s[i]=='B' and s[j]=='G'):
            ans += r_nokori[j+1]
            if 2*j-i <= n:
                if s[2*j-i] == 'R': ans-= 1

        if (s[i]=='B' and s[j]=='R') or (s[i]=='R' and s[j]=='B'):
            ans += g_nokori[j+1]
            if 2*j-i <= n:
                if s[2*j-i] == 'G': ans-= 1

print(ans)
 