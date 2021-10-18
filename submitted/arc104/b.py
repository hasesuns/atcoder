import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, s = input().split()

n = int(n)
s = list(s)

array_sum = 0
cnt_a = 0
cnt_t = 0
cnt_g = 0
cnt_c = 0
ans = 0

for left in range(n):
    cnt_a=cnt_t=cnt_c=cnt_g=0
    if s[left] == 'A': cnt_a=1
    elif s[left] == 'T': cnt_t=1
    elif s[left] == 'C': cnt_c=1
    else: cnt_g=1

    for right in range(left+1, n):

        if s[right] == 'A': cnt_a+=1
        elif s[right] == 'T': cnt_t+=1
        elif s[right] == 'C': cnt_c+=1
        else: cnt_g+=1

        if cnt_a==cnt_t and cnt_c==cnt_g:
            ans+=1


print(ans)
 