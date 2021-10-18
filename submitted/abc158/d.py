from collections import deque

s = input()
q = int(input())

queue = deque(list(s))
is_reverse = False

for _ in range(q):
    tfc = input()
    if tfc[0] == '1':
        is_reverse = not is_reverse
        continue
    else:
        if is_reverse == False and tfc[2] == '1':
            queue.appendleft(tfc[4])
        elif is_reverse == False and tfc[2] == '2':
            queue.append(tfc[4])
        elif is_reverse == True and tfc[2] == '1':
            queue.append(tfc[4])
        elif is_reverse == True and tfc[2] == '2':
            queue.appendleft(tfc[4])

if is_reverse:
    ans = list(queue)
    new_ans = ans[::-1]
    print(*new_ans, sep='')
else:
    ans = queue
    print(*ans, sep='')