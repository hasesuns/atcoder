import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

s, t = input().split()

def standard(S):
    if S[0] == 'B':
        return -int(S[1])+1

    else:
        return int(S[0])

ss = standard(s)
tt = standard(t)

print(abs(ss-tt))