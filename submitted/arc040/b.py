import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, r = map(int, input().split())
s = input() #sys.stdin.readlineは最後が改行

last = s.rfind('.')
if last == -1:
    print(0)
    exit()

s = list(s)

ans = 0
diff = n-r
i = 0
while i + r -1 < last:
    if s[i] == '.':
        for j in range(r):
            s[i+j]='o'
        ans+=1
    else:
        ans+=1
        i+=1

ans += 1

print(ans)