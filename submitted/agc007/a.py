h,w,= map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]

cnt = 0
for i in range(h):
    cnt += input().count('#')

short = h+w-1

if cnt == short:
    print('Possible')
else:
    print('Impossible')