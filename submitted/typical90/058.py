import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())

def calc(x):
    x_num_list = list(str(x))
    y = 0
    for i in x_num_list:
        y += int(i)        
    z = (x + y) % 100000
    return z

res_list = [n]
res_set = {n}
tmp = n
loop_begin_idx = 0
loop_end_idx = 0
loop_list = []

while True:
    tmp = calc(tmp)
    if tmp in res_set:
        loop_begin_idx = res_list.index(tmp)
        loop_end_idx = len(res_list)
        loop_list = res_list[loop_begin_idx:loop_end_idx]
        break
    res_list.append(tmp)
    res_set.add(tmp)

if k < loop_end_idx:
    print(res_list[k])
    exit()

k_idx_in_loop = (k - loop_begin_idx) % len(loop_list)
ans = loop_list[k_idx_in_loop]
print(ans)