k = int(input())

from collections import deque
queue = deque([1,2,3,4,5,6,7,8,9])

count = 0

while queue:
    now = queue.popleft()
    count += 1
    if count == k:
        print(now)
        exit()
    now_ = now%10
    if now_ == 0:
        queue.append(10*now+now_)
        queue.append(10*now+now_+1)
    elif now_ == 9:
        queue.append(10*now+now_-1)
        queue.append(10*now+now_)
    else:
        queue.append(10*now+now_-1 )
        queue.append(10*now+now_)
        queue.append(10*now+now_+1)