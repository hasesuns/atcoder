import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
import numpy as np

n = int(input())
ab = [tuple(map(int,input().split())) for i in range(n-1)]
es = [[] for i in range(n)]
for i, (a,b) in enumerate(ab):
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)

class TREE(object):
    def __init__(self, G, root=0):
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.n)]
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.dfs()

    def dfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for v in self.G[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]


depth = np.array(TREE(es).depth)

ans = [0]*n

zero = one = two = n // 3
if n % 3 == 1: one += 1
if n % 3 == 2:
    one+=1
    two+=1

num_odd = np.count_nonzero(depth %2 == 1)

if num_odd <= n/3:
    for i in range(n):
        if depth[i] % 2 == 1:
            if zero > 0:
                ans[i] = zero*3
                zero -= 1
        else:
            if two > 0:
                ans[i] = two*3 - 1
                two -= 1
            elif one > 0:
                ans[i] = one*3 - 2
                one -= 1
            elif zero > 0:
                ans[i] = zero*3
                zero -= 1
            else:
                break
    else:
        print(*ans, sep=' ')
        exit()

if num_odd >= n/3*2:
    for i in range(n):

        if depth[i] % 2 == 0:
            if zero > 0:
                ans[i] = zero*3
                zero -= 1
        else:
            if two > 0:
                ans[i] = two*3 - 1
                two -= 1
            elif one > 0:
                ans[i] = one*3 - 2
                one -= 1
            elif zero > 0:
                ans[i] = zero*3
                zero -= 1
            else:
                break
    else:
        print(*ans, sep=' ')
        exit()


for i in range(n):
    if depth[i] % 2 == 0:
        if one > 0:
            ans[i] = one*3 - 2
            one -= 1
        elif zero > 0:
            ans[i] = zero*3
            zero -= 1
        else:
            break
    else:
        if two > 0:
            ans[i] = two*3 - 1
            two -= 1
        elif zero > 0:
            ans[i] = zero*3
            zero -= 1
        else:
            break
else:
    print(*ans, sep=' ')
    exit()

 