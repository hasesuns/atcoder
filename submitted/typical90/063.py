import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
from collections import Counter

h, w = map(int, input().split())
table = [list(map(int,input().split())) for _ in range(h)]    
ans = 0
        
for i in range(1, 2**h):
    use_row_idx_list = [j for j in range(h) if (i >> j) & 1]
    counter = Counter()
    for col in range(w):
        use_num = table[use_row_idx_list[0]][col]
        if all(table[row][col] == use_num for row in use_row_idx_list):
            counter[use_num] += 1
    if counter:
        ans = max(ans, len(use_row_idx_list) * counter.most_common()[0][1])
            
print(ans)