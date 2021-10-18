from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
py = [tuple(map(int,input().split())) for i in range(m)]

# data_list = []
# i = 0
# for p,y in py:
#     data_list.append([i,p,y])
#     i += 1
ans = [0]*m

p_yi_table = [[] for i in range(n+1)]
for i,(p,y) in enumerate(py):
    p_yi_table[p].append((y,i))
for p, yi_list_by_p in enumerate(p_yi_table):
    yi_list_by_p.sort()
    for j,(y,i) in enumerate(yi_list_by_p):
        s = str(p).zfill(6) + str(j+1).zfill(6)
        ans[i] = s

print(*ans, sep='\n')