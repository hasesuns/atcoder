s = input()
n = len(s)
ans = [0]*n


rside=0
lside=0

rpoint=0
lpoint=0

radd = 0
ladd = 0

left = 0
right=0
while right<n:
    if right == n-1:
        ladd = (rpoint - left + 1 ) // 2 +1
        radd = rpoint - left + 1 - ladd

        radd +=  (right - lpoint + 1) // 2 + 1
        ladd +=  (right - lpoint + 1) - ((right - lpoint + 1) // 2 + 1)

        ans[rpoint] += radd
        ans[lpoint] += ladd


    elif s[right] =='R' and s[right+1] == 'L':
        rpoint = right
        lpoint = right+1
    elif s[right] =='L' and s[right+1] == 'R' :
        ladd = (rpoint - left + 1 ) // 2 + 1
        radd = rpoint - left + 1 - ladd

        radd +=  (right - lpoint + 1) // 2 + 1
        ladd +=  (right - lpoint + 1) - ((right - lpoint + 1) // 2 + 1)

        ans[rpoint] += radd
        ans[lpoint] += ladd

        left = right+1
        
    right += 1

print(*ans)